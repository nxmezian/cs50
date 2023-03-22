#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    //formula for rayscaling an image by assigning the average color of blue, green and red values
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j <  width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int red = image[i][j].rgbtRed;

            float average_color = round((blue + green + red) / 3.0);

            image[i][j].rgbtBlue = average_color;
            image[i][j].rgbtGreen = average_color;
            image[i][j].rgbtRed = average_color;

        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //Formula for converting image to sepia
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j <  width; j++)
        {
            float blue = image[i][j].rgbtBlue;
            float green = image[i][j].rgbtGreen;
            float red = image[i][j].rgbtRed;

            int sepia_red = round((.393 * red) + (0.769 * green) + (0.189 * blue));
            if (sepia_red > 255)
            {
                sepia_red = 255;
            }
            int sepia_green = round((.349 * red) + (0.686 * green) + (0.168 * blue));
            if (sepia_green > 255)
            {
                sepia_green = 255;
            }
            int sepia_blue = round((.272 * red) + (0.534 * green) + (0.131 * blue));
            if (sepia_blue > 255)
            {
                sepia_blue = 255;
            }

            image[i][j].rgbtBlue = sepia_blue;
            image[i][j].rgbtGreen = sepia_green;
            image[i][j].rgbtRed = sepia_red;


        }
    }


    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    //formule for mirroring image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j <  width / 2; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Formula for blurring an image
    return;
}
