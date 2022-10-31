// Kata url: https://www.codewars.com/kata/57c1ab3949324c321600013f.
const char TRANSLATE_TABLE[26] = "@8(D3F6#!JK1MN0PQR$7UVWXY2";

char* toLeetSpeak(char *speak)
{
    for (int i = 0; speak[i]; i++) {
        if (speak[i] >= 'A' && speak[i] <= 'Z') {
            speak[i] = TRANSLATE_TABLE[speak[i] - 'A'];
        }
    }
    return speak;
}
