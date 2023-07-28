import subprocess

command = ["python3","/Users/ananyasachdev/project-01/test.py" , "arg1", "arg2"]

try:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.wait()

    if return_code != 0:
        # Handle the error
        err = stderr.decode(encoding='utf-8').split('\n')
        print(f"Error: Return code {return_code}")
        # print("Error message:", err)
        # for i in err:
        #     print(i)
        print(err[4])                   #index 4 contains the error
        err_type = err[4].split()[0].replace(":","")
        print("error type:", err_type )
        err_msg_index = err[4].find(":")
        err_msg = err[4][err_msg_index + 2:]
        print("error message:" ,err_msg)
        print()
    else:
        # Process the output
        print(stdout.decode().strip())
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")

