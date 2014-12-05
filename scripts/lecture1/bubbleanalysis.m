I = imread('bubbles.png');
BW = rgb2gray(I);
E = edge(BW, 'canny');
F = imfill(E, 'holes');
result = regionprops(F);

areas = zeros(size(result));
for i = 1:size(result)
    areas(i) = result(i).Area;
end

figure(1);
subplot(3,2,1); imshow(I); title('Original image');
subplot(3,2,2); imshow(BW); title('BW image');
subplot(3,2,3); imshow(E); title('Edge detection');
subplot(3,2,4); imshow(F); title('Image filling');
subplot(3,2,5:6); hist(areas,30); title('Histogram of bubble area (px)');

