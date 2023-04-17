imax = np.argmax(A[col:,col])
imax += col # Correct index with offset since argmax returns index in A[col:,col], not A[:,col]