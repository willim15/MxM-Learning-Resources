#pragma once

#include "ofMain.h"

class ofApp : public ofBaseApp{
    
public:
    void setup();
    void update();
    void draw();
    void keyPressed(int key);
    
    unsigned char* imageStored;
    unsigned char* imageStored2;
    unsigned char* imageStored3;
    
    int visualWIDTH;
    int visualHEIGHT;
    
    int switchCase;
    int columnNum;
    int rowNum;
    
    ofImage slitScanImage;
    ofVideoGrabber myVideoGrabber;
    ofTexture myTexture;
    
    ofTrueTypeFont myFont;
    
private:
    void movePixelsInImage(ofImage * image);
};
