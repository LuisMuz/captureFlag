# sudo -r fog

In his unconscious state, R-boy's vision is all mixed up.
The images he sees seem to be indecipherable, as if the pixels had been randomly shuffled, but he knows that the seed of the solution is within what he sees.

Suddenly, R-boy finds a sheet of paper with written notes:

```
np.random.seed(seed)
indices = np.random.permutation(len(pix))
...
stepic.encode(img, message)
...
imutils.rotate(img, angle=rot_angle)
```

Hint: once the image is reconstructed, each sub-block of the board will contain steganographed binary message, e.g., 010111. The two most significant digits represent how much it has been rotated, e.g., 01 = 90°, and the remaining four represent its original position, e.g., 0111 = 7, since it starts at 0, the original position of this block was 8th.

**IMPORTANT!** - Some tools for opening encrypted zip files show some issues in decrypting the zip containing the flag. Please don't trust the windows explorer unzip tool on Windows machine or unzip also in Unix machine. Use instead other tools such as for example 7zip.