# Check log
 - Add your private key
 - Set up inventory file
 - Change variables in main.py:
   - **slow** - The number of long requests, after which the entire chain of long requests will be tracked and displayed in a file
   - **fast** - The number of fast requests, after which the long request chain is reset
   - **t** - The duration of the request in milliseconds, if the request is executed >= **t** is a long request
 - And run: ansible-playbook ./check_log.yml --private-key ./id_rsa
