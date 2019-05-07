from __future__ import print_function
from IPython.core.magic import Magics, magics_class, cell_magic

@magics_class
class ExpectMagic(Magics):

    def _run_(self, code):
        execution = self.shell.run_cell(code)
        execution.raise_error()
        return execution.result
    
    @cell_magic
    def expect(self, line, cell):
        print('Expected:')
        expected = self._run_(line)
        print('Got:')
        got = self._run_(cell)
        assert got == expected, 'expected: {0}, got: {1}'.format(expected, got)
        print('Success!　🎉')


def load_ipython_extension(ipython):
    ipython.register_magics(ExpectMagic)
    