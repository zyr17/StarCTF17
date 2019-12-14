#include <bits/stdc++.h>

char pswd[][111] = {"Welcome","to","paly","CTF","in","sixstars","and","Hack","for","fun"};

int main(){
    for (;;){
        char c = getchar();
        if (c >= '0' && c <= '9')
            std::cout << pswd[c - '0'] << std::endl;
        fprintf(stderr, "%c", c);
    }
}