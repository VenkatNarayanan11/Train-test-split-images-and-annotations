# Train-test-split-images-and-annotations
Use this script to split your images (any format) and annotations (any format) into train and test/valid folders. 

---

### Table of Contents

- [Description](#description)
- [Technologies](#technologies)
- [License](#license)
- [Author Info](#author-info)

---

## Description

In machine learning, having a clean dataset is the most necessary step of all. However, it's not always easy to work with a huge dataset. After hours of pre-processing and annotating, there comes the splitting of dataset into train/valid/test or simply train/test. I had a hard time finding a quick solution online to split my images and labels/annotations directory into train/valid. So, I wrote a simple Python script that takes care of this job. The script works for most format of images (.jpg, .png, .jpeg) / labels (.txt, .xml, .csv) and also is easy to edit and reproduce for your convenience. To summarize, the script accepts input path to the source images and labels folder and outputs two folders such as train and valid containing the split images and labels in separate subfolders. The python script "split.py" has comments that will walk you through the entire steps.  

#### Technologies

- Python
- Scikit-learn

[Back To The Top](#Train-test-split-images-and-annotations)

---

## License

MIT License

Copyright (c) [2021] [Venkat Narayanan Balachandran]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#Train-test-split-images-and-annotations)

---

## Author Info

- LinkedIn - [Venkat_Narayanan_Balachandran](https://www.linkedin.com/in/venkat-balachandran)

[Back To The Top](#Train-test-split-images-and-annotations)
