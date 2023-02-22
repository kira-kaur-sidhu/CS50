// Filter More (helper.c file)
// Implement the functions in helpers.c such that a user can apply grayscale, reflection, blur, or edge detection filters to their images.
  // The function grayscale should take an image and turn it into a black-and-white version of the same image.
  // The reflect function should take an image and reflect it horizontally.
  // The blur function should take an image and turn it into a box-blurred version of the same image.
  // The edges function should take an image and highlight the edges between objects, according to the Sobel operator.

#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
        {
            float average_value = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) * .3333;
            image[i][j].rgbtRed = round(average_value);
            image[i][j].rgbtGreen = round(average_value);
            image[i][j].rgbtBlue = round(average_value);
        }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
        for (int j = 0, n = width-1; j < width/2; j++, n--)
        {
            RGBTRIPLE tmp= image[i][j];
            image[i][j] = image[i][n];
            image[i][n] = tmp;
        }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];

    // Copy Array into Temporary Array
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
            tmp[i][j] = image[i][j];

    // Update color values
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
        {
            float total_red = 0;
            float total_green = 0;
            float total_blue = 0;
            int counter = 0;

            for (int k = i-1; k < i+2; k++)
                for (int l = j-1; l < j+2; l++)
                {
                    if (k >= height || k < 0 || l >= width || l < 0)
                        continue;

                    else
                    {
                        total_red += tmp[k][l].rgbtRed;
                        total_green += tmp[k][l].rgbtGreen;
                        total_blue += tmp[k][l].rgbtBlue;
                        counter += 1;
                    }
                }

            image[i][j].rgbtRed = round(total_red / counter);
            image[i][j].rgbtGreen = round(total_green / counter);
            image[i][j].rgbtBlue = round(total_blue / counter);
        }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{

    // Copy Array into Temporary Array
    RGBTRIPLE tmp[height][width];
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
            tmp[i][j] = image[i][j];

    // Create sobel array
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Change values in image
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
        {
            float Gx_red = 0;
            float Gy_red = 0;
            float Gx_green = 0;
            float Gy_green = 0;
            float Gx_blue = 0;
            float Gy_blue = 0;

             for (int k = -1; k < 2; k++)
                for (int l = -1; l < 2; l++)
                {
                    if (i + k >= height || i + k < 0 || j + l >= width || j + l < 0)
                        continue;
                    else
                    {
                        Gx_red += tmp[i + k][j + l].rgbtRed * Gx[k + 1][l + 1];
                        Gy_red += tmp[i + k][j + l].rgbtRed * Gy[k + 1][l + 1];
                        Gx_green += tmp[i + k][j + l].rgbtGreen * Gx[k + 1][l + 1];
                        Gy_green += tmp[i + k][j + l].rgbtGreen * Gy[k + 1][l + 1];
                        Gx_blue += tmp[i + k][j + l].rgbtBlue * Gx[k + 1][l + 1];
                        Gy_blue += tmp[i + k][j + l].rgbtBlue * Gy[k + 1][l + 1];
                    }
                }

            int red = round(sqrt(pow(Gx_red,2) + pow(Gy_red,2)));
            int green = round(sqrt(pow(Gx_green,2) + pow(Gy_green,2)));
            int blue = round(sqrt(pow(Gx_blue,2) + pow(Gy_blue,2)));

            if (red > 255)
                red = 255;
            if (green > 255)
                green = 255;
            if (blue > 255)
                blue = 255;

            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }

    return;
}
