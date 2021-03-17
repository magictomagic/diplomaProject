clear;clc;close all;
G1 = randn(100,2).*1+3;
G2 = randn(100,2).*1;
G3 = randn(100,2).*1-3;
X = [G1;G2;G3];
k = 4;
cls = kmeans(X,k);
figure(1)
subplot(1,2,2)
Legends = {'r.','b.','g.', 'o'};
hold on
for i = 1:4
    plot(X(find(cls==i),1),X(find(cls==i),2),Legends{i})
end
hold off
title('results')
subplot(1,2,1)
plot(X(:,1),X(:,2),'.')
title('initial data')