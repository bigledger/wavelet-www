
1) I have forked the repository https://github.com/bigledger/blg-www and become https://github.com/bigledger/wavelet-www  
   I cloned the current files / folder from "blg-www", because it can help us to get started faster. I would like to do a new website (lets call it "wavelet-www"), hence, many things need to change.
   Just a bit of background for you:
     Previously, we host our https://wavelet.net with WpEngine.com , a wordpress website hosting provider. But we are no longer paying them, and the website is currently down.
   first of all, the wavelet-www is currently hosted at WP Engine, and i have stopped paying recently, and the wordpress server is shutdown. But I have not setup the wavelet-www yet. Let me share with you the following information:

   * My godaddy api credentials is stored in the following home directory : ~/.aimatrix/credentials/godaddy.txt
   * if you look at ~/.aws/credentials file, there are 2 profiles, [web-publisher] and [admin@aimatrix.com] both will have access to the aws cloud account, to conf
igure the ACM certificate, aws cloud front, s3 buckets etc. 

 * For each of the task below, you can use several sub-agents to work on them


2) Tips
   As I have initialized this folder, by "forking" from the blg-wiki to blg-www , and I haven't setup the cloudfront, the ACM certificate, the Godaddy DNS server configurations yet, so, we may have to do these setup and configurations.
   As we forked from blg-www to wavelet-www, i don't want you to screw up, so all the github actions, and codes that push to the remote, configurations need to be inspected in detailed, to make sure nothing screw up  and ensure you are NOT mixing up both website.
    So, blg-www => https://www.bigledger.com => https://bigledger.com (https://github.com/bigledger/blg-www)
    and wavelet-www => https://www.wavelet.net => https://wavelet.net (https://github.com/bigledger/wavelet-www)
   For the configurations of the wavelet-www , you can take a peek at the other websites i have configured in the AWS cloudfront s3, for example https://bigledger.com etc... (please ensure you don't mix them together , don't screw up, i am just asking you to see only)
   I am aware that as this is the apex domain name, due to limitations of goDaddy, i may need to manually configure the domain forwarding in the GoDaddy website to forward bigledger.com to www.bigledger.com itself

3) Our priorities as follow:
  a) Get the website https://wavelet.net  up and running first, even with the content from the wavelet-www NOT suitable and need refinement.
     - This means, you need to configure a new s3 bucket, for the blg-www , configure the acm certificate, update the godaddy DNS record, and update the cloud front, and perform the testing for this.
  b) Next, do some research online, and understand that wavelet.net is focusing on Point of Sales and ERP, while BigLedger is focusing on "Business Operating System", and this website is for Wavelet, you will generate the content that is suitable for Wavelet, focusing on ERP and Point of Sales, instead of data hub or business operating system.

* Please make use of multiple sub-agents to execute this in parallel.




