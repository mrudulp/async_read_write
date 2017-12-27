def read_data(file_obj):
    '''
        Lazily Reads Data from given file object.
        As a result one can read a really long file and at the sametime process on the read data.
        Args:
            file_obj (file): handle to file 
    '''
    while True:
        line = file_obj.readline()
        if not line:
            break

        yield line

def write_data(file_obj, data):
    '''
        Writes Data passed to method to the file
        Args:
            file_obj (file): Handle to the file
            data (str): Data that needs to be written
    '''
    file_obj.write(data)

def isint(int_str):
    '''
        Validates if the string contains integer or not
        Args:
            int_str (str): String containing integer
    '''
    try:
        int(int_str)
        return True
    except ValueError:
        return False

def read_write_data(in_file, out_file, iter_stop_idx):
    '''
        Reads and writes to the file till iter_stop_idx
        Reads from file till data is available (assumes in_file has 50 sequential integers[0..50] )
        Remaining numbers are auto incremented till it reaches iter_stop_idx.
        Args:
            in_file (str): File name that needs to be read
            out_file (str): That needs to be written
            iter_stop_idx (int): Index number where iterator has to stop
    ''' 
    _write_count = 0
    _prev_data = 0
    with open(out_file, 'w+') as fout:
        with open(in_file, 'r') as fin:
            while True:
                data = next(read_data(fin), None)
                if data and isint(data):
                    _prev_data = int(data)
                else:
                    _prev_data += 1
                    if _write_count == iter_stop_idx:
                        print "Done Iterating over file"
                        break
                data = "{0}\n".format(_prev_data)
                print data
                write_data(fout, data)
                _write_count += 1

IN_FILE = "in_file.txt"
OUT_FILE = "out_file.txt"
ITER_STOP_IDX = 100
read_write_data(IN_FILE, OUT_FILE, ITER_STOP_IDX)
