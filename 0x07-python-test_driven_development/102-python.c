#include <Python.h>

/**
 * print_python_string - Print a nice representation of python string
 * @p: A pointer to the python object containing the string
 *
 * Return:void
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;

	printf("[.] string object info\n");

	if (PyUnicode_Check(p) == 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	len = PyUnicode_GET_LENGTH(p);
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}
