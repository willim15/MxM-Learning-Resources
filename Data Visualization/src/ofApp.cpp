#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    VISUALwidth = "\Documents\DataVisualization\SCWIDTH"
    VISUALheight = "\Documents\DataVisualization\SCHEIGHT"
    columnNum = 0;
    rowNum = 0;
    switchCase = 1;
        
    LiveHeatGraph.setDesiredFrameRate(60);
    LiveHeatGraph.initGrabber(VISUALwidth, VISUALheight);
    
    imageStored = new unsigned char [VISUALwidth * VISUALheight * 3];
    imageStored2 = new unsigned char [VISUALwidth * VISUALheight * 3];
    imageStored3 = new unsigned char [VISUALwidth * VISUALheight * 3];
    
    myTexture.allocate (VISUALwidth, VISUALheight, GL_RGB);
    OverlayGraphImage.allocate (VISUALwidth, VISUALheight, OF_IMAGE_COLOR);
    ofSetVerticalSync(true);
    
}

//--------------------------------------------------------------
void ofApp::update(){
    LiveHeatGraph.update();
    
    switch (switchCase) {
        case 1:
            if (LiveHeatGraph.isFrameNew()) {
                unsigned char* pixelData = LiveHeatGraph.getPixels().getData();
                int rowNumPixels, columnNumPixels, mouseXPixels;
                
                for (int row = 0; row < VISUALheight; row++) {
                    rowNumPixels = row * VISUALwidth * 3;
                    for (int cc = 0; cc < 3; cc++) {
                        columnNumPixels = columnNum * 3;
                        mouseXPixels = mouseX * 3;
                        imageStored[rowNumPixels + columnNumPixels +cc] = pixelData [rowNumPixels + mouseXPixels + cc];
                    }
                }
                columnNum ++;
                myTexture.loadData(imageStored, VISUALwidth, VISUALheight, GL_RGB);
            }
            break;
        case 2:
            if (LiveHeatGraph.isFrameNew()) {
                unsigned char* pixelData = LiveHeatGraph.getPixels().getData();
                int rowNumPixels, columnNumPixels, mouseXPixels;
                int v1 = ofRandom(0, 8);
                
                for (int column = 0; column < VISUALwidth; column++) {
                    columnNumPixels = column * VISUALheight * 3;
                    for (int cc = 0; cc < v1; cc++) {
                        rowNumPixels = rowNum * 3;
                        mouseXPixels = mouseX *3;
                        imageStored2[columnNumPixels + rowNumPixels +cc] = pixelData [columnNumPixels + mouseXPixels + cc];
                    }
                }
                rowNum ++;
                myTexture.loadData(imageStored2, VISUALwidth, VISUALheight, GL_RGB);
            }
            break;
        case 3:
            if (LiveHeatGraph.isFrameNew()) {
                unsigned char* pixelData = LiveHeatGraph.getPixels().getData();
                unsigned char* imageStored3 = OverlayGraphImage.getPixels().getData();
                
                movePixelsInImage(&OverlayGraphImage);
                
                for (int x = 0; x < VISUALwidth; x++) {
                    for (int cc = 0; cc <3 ; cc++) {
                        int imagePostion = ((VISUALwidth * VISUALheight *3)) + (x) * 3;
                        int videoPostion = (x) * 3;
                        
                        imageStored3[imagePostion + cc] = pixelData[videoPostion + cc];
                        
                    }
                }
            }
            break;
        default:
            //Nothing here
            break;
    }
}

void ofApp::movePixelsInImage (ofImage * image) {
    unsigned char * pixelData = image -> getPixels().getData();
    for (int column = 0; column < image->getWidth() - 1; column++ ) {
        for (int row = 0; row < image -> getHeight(); row++) {
            for (int cc = 0; cc < 3; cc++) {
                int postion = row * (image -> getWidth() * 3) + column * 3;
                int nextPostion = postion + VISUALwidth * 3;
                pixelData[postion + cc] = pixelData[nextPostion + cc];
                
            }
        }
    }
    image-> update();
}


//--------------------------------------------------------------
void ofApp::draw(){
    LiveHeatGraph.draw(0,0);
    
    if (switchCase == 1 || switchCase == 2) {
        ofDrawLine(mouseX, 0 , mouseX, VISUALheight);
    } else {
        ofDrawLine(0, 2, VISUALwidth, 2);
    }
    
    myFont.drawString("Press either: 1, 2, or 3 ", 50, VISUALheight + 50);
    myFont.drawString("Graph Displayed: ", (3 * ofGetWidth() )/ 4 - 200, VISUALheight + 50);
    string switchCaseString = to_string(switchCase);
    myFont.drawString(switchCaseString, (3 * ofGetWidth() )/ 4 + 10, VISUALheight + 50);
    
    if (switchCase == 1) {
        myTexture.draw(650, 0);
    }
    if (switchCase == 2) {
        myTexture.draw(650, 0);
    }
    if (switchCase == 3) {
        OverlayGraphImage.draw(650, 0);
    }
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    if (key == '1'){
        switchCase = 1;
    } else if (key == '2') {
        switchCase = 2;
    } else if (key == '3') {
        switchCase = 3;
    }
}

