abs_col = np.abs(A[column:, column])
dummy, index = np.max(abs_col), np.argmax(abs_col)
index = index + column
