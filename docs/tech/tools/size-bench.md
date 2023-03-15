# Size Bench

SizeBench is a utility that analyzes PDB information to help you optimize and reduce the size of your binaries (DLLs, EXEs, and other PE files). You can break down a binary by sections of the PE file, COFF Groups, static libraries, OBJ file, even by source file - to see which parts of your code and data contribute meaningfully to on-disk and in-memory size. SizeBench can also run heuristic analyses to help you find likely sources of waste, including inefficient usage of virtual functions, duplicated data, and C++ templated code that is "almost foldable" to look for quick opportunities to reduce size.

- Store: <https://www.microsoft.com/en-us/p/sizebench/9ndf4n1wg7d6#activetab=pivot:overviewtab>
- Blog Post: <https://devblogs.microsoft.com/performance-diagnostics/sizebench-a-new-tool-for-analyzing-windows-binary-size/>
