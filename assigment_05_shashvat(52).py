# Program to find Longest Common Subsequence using Dynamic Programming
def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # Create a table of size (m+1) x (n+1)
    lcs_table = [[0 for j in range(n + 1)] for i in range(m + 1)]
    # Fill the table
    for i in range(m + 1):
        for j in range(n + 1):
            # If either sequence is empty
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            # If characters are same
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            # If characters are different
            else:
                if lcs_table[i - 1][j] > lcs_table[i][j - 1]:
                    lcs_table[i][j] = lcs_table[i - 1][j]
                else:
                    lcs_table[i][j] = lcs_table[i][j - 1]
    # Length of LCS
    index = lcs_table[m][n]
    # Create an array to store LCS
    lcs_string = [''] * index
    i = m
    j = n
    # Trace back to find the LCS
    while i > 0 and j > 0:
        # If characters are same
        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i = i - 1
            j = j - 1
            index = index - 1
        # Move in the direction of larger value
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i = i - 1
        else:
            j = j - 1
    return ''.join(lcs_string)
# Main program
X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")
result = LCS(X, Y)
print("Longest Common Subsequence:", result)
print("Length of LCS:", len(result))
