# Jatan Pandya
# ECE - 241
# HW - 2 : P3.py
# Python Class for representing two-dimensional matrices

class Matrix:
	def __init__(self, name, row, col):
		self.name = name
		self.row = row
		self.col = col
		self.m = [[-1] * self.col for x in range(self.row)]  # initialized, set to -1
		print(f"\nThe Matrix '{self.name}' is initialized as follows --> \n{self.m}")
	
	def input_matrix(self):
		"""
		updates earlier initialized self.m matrix in place with user defined values
		:return: nil
		:rtype: nil
		"""
		print("\nEnter your integer values for the elements of the matrix [by row] --> \n")
		self.m = [[int(input()) for x in range(self.col)] for y in range(self.row)]
	
	def __repr__(self):
		return f"{self.__class__.__name__}(row={self.row},col={self.col})"
	
	def __str__(self):
		"""
		:return: string rep of matrix. a proper two-dimensional representation of the matrix elements
		:rtype: str
		"""
		res = ''
		for i in self.m:
			for j in i:
				res += ' ' + f"{str(j):<5}" + ' '
			res += '\n'
		return f"\nMatrix '{self.name}' is as follows --> \n [{res.strip()}]"
	
	def __eq__(self, other):
		"""
		:param other: Object 2 of matrix '2'
		:type other: Object of class Matrix
		:return: boolean value for comparison
		:rtype: BOOL
		"""
		if isinstance(other, Matrix):
			if self.m == other.m:
				return True
		return False


if __name__ == '__main__':
	mat = Matrix
	while True:
		name_1 = input("\nEnter the name of the first matrix: ")
		row_1 = int(input(f"\nEnter number of rows for matrix '{name_1}': "))
		col_1 = int(input(f"\nEnter number of columns for matrix '{name_1}': "))
		
		matrix_1 = mat(name_1, row_1, col_1)
		matrix_1.input_matrix()
		print(matrix_1)
		print("\nSuccessfully overloaded the __str__ method.")
		
		switch1 = input(f"\nIs the above matrix '{name_1}' correct? Enter 'yes' to continue or 'no' to try again: \n")
		if switch1.lower().strip() == 'no':
			continue
		if switch1.lower().strip() == 'yes':
			break
	
	while True:
		name_2 = input("\nEnter the name of the second matrix: ")
		row_2 = int(input(f"\nEnter number of rows for matrix '{name_2}': "))
		col_2 = int(input(f"\nEnter number of columns for matrix '{name_2}': "))
		
		matrix_2 = mat(name_2, row_2, col_2)
		matrix_2.input_matrix()
		print(matrix_2)
		print("\nSuccessfully overloaded the __str__ method.")
		
		switch2 = input(f"\nIs the above matrix '{name_2}' correct? Enter 'yes' to continue or 'no' to try again: \n")
		if switch2.lower().strip() == 'yes':
			print(f'\nMatrix {name_1} --> ', repr(matrix_1))
			print("Successfully overloaded the __repr__ method.")
			print(f'\nMatrix {name_2} --> ', repr(matrix_2))
			print("Successfully overloaded the __repr__ method.")
			print(f"\nNow is Matrix {name_1} equal to Matrix {name_2} ? --> {matrix_1 == matrix_2}")
		else:
			continue
		break
