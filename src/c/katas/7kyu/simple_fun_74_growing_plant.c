// Kata url: https://www.codewars.com/kata/58941fec8afa3618c9000184.

int growingPlant(int upSpeed, int downSpeed, int desiredHeight)
{
    int my_plant = 0;
    int days = 0;

    while (my_plant < desiredHeight) {
        my_plant += upSpeed;
        days++;
        if (my_plant >= desiredHeight) {
            break;
        }
        my_plant -= downSpeed;
    }
    return days;
}