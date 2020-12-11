from bs4 import BeautifulSoup
import requests
import csv
import os
i = 1
os.mkdir('All_images')
for i in range(65):
    source = requests.get('https://undraw.co/api/illustrations?page='+str(i)).text

    soup = BeautifulSoup(source, 'lxml')

    # image_link = f'https:{svg_img1}'
    
    csv_file = open('crawl_by_webNumber'+str(i)+'.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Image_Titles', 'Image_links'])

    img_src = soup.p.text
    #print(img_src) 

    img = img_src.split('[')[1]
    img1 = img.split('{')

    # to check 'number of items
    num = len(img1)

    count = 1
    while (count < num):
        img2 = img.split('{')[count]
        count = count + 1
        # print(img2)

        # code for Title

        try:
            title = img2.split(',')[1]
            title1 = title.split(':')[1]
            titles = title1.split('"')[1]
            print(titles)
        except Exception as e:
            raise e

        # code for image link

        try:
            img3 = img2.split(',')[2]
            svg_img = img3.split(':')[2]
            svg_img1 = svg_img.split('"')[0]
            image_link = f'https:{svg_img1}'
            print(image_link)
        except Exception as e:
            raise e

        csv_writer.writerow([titles, image_link])

        img_data = requests.get(image_link).content
        with open("All_images/"+f'{titles}'+'.svg', 'wb+') as f:
            f.write(img_data)

    csv_file.close()

    i += 1

        
