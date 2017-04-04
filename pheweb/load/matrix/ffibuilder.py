
import cffi
import os.path

cxx_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'matrixify.cpp')
with open(cxx_path) as f:
    src = f.read()

ffibuilder = cffi.FFI()
ffibuilder.set_source('pheweb.load.matrix._matrixify',
                      src,
                      source_extension='.cpp',
                      extra_compile_args=['--std=c++11'],
)
ffibuilder.cdef("int cffi_run(char *sites_fname, char *augmented_pheno_glob, char *matrix_fname);")
