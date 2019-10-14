Problem 1:

Section 1: Kernel Trick

Varous kernels were used as an attempt to make the given linearly inseperable data in 2-D into linearly seperable 3-D data. The kernels used are as follows:
(1) z=x\^2+y\^2
(2) z=x\*y
(3) z=x\^3+y\^3
(4) z=x\^4+y\^4
Among the above kernels tried, kernels (1) and (4) led to the data becoming linearly seperable with accuracy 1.0. Kernels (2) and (3) led to linearly inseperable data with accuracy 0.58 and 0.66 respectively. The graphical illustrations have been provided in 'Report.pdf'.

Section 2: Letter Classification

The kernel types 'linear', 'polynomial' and 'rbf' provided results with considerable scores. These were tried for different values of parameter 'C' for svm.SVC() function. The best results observed were obtained from RBF Kernel at C=1.0. which provided almost 94% accuracy in everyfold. The scores for each fold for each kernel type have been included in the file 'Report.pdf'.
