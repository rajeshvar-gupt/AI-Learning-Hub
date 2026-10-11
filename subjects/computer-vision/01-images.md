# CV-001 · Images, channels and preprocessing

Prerequisite: DL-005.

Outcome: describe an image array and preserve its meaning through preprocessing.

A grayscale image is a height-by-width array; an RGB image has three ordered color channels. The digits lab uses arrays shaped (batch, 8, 8), with intensities from 0 to 16 before conversion. Dividing by the known scale 16 gives values in [0,1] without estimating statistics from held-out data. A camera pipeline may use different scales or channel orders; document them rather than guessing.

Cropping selects a region, resizing changes the sampling grid, and interpolation estimates new pixel values. Distorting aspect ratio can alter meaningful shapes. Thresholding converts intensities into a binary mask; a global threshold can fail under uneven lighting. A smoothing filter suppresses some high-frequency detail, including useful edges. Image processing operations are not automatically learned classifiers.

Use a data contract: expected size, channel order, dtype, range and missing/corrupt-image policy. Keep training and inference preprocessing consistent. A horizontal flip is plausible augmentation for some objects but can change the meaning of text. Choose label-preserving transformations and apply training augmentation only after splitting.

Images from the same patient, video, scene or writer can be highly dependent. Split by the intended deployment unit where IDs are available; random image splitting can leak identity or near-duplicates. The bundled digits demonstration uses random stratified splits and makes no new-writer guarantee.

[Questions](../../assignments/CV-001/questions.md) · [Solutions](../../assignments/CV-001/solutions.md) · [CNN project](../../projects/intermediate/digits-cnn/README.md) · [Module index](README.md)
