
1) The current folder was copied from https://github.com/bigledger/blg-wiki and become https://github.com/bigledger/blg-www  
   I cloned the current files / folder from "blg-wiki", because it can help us to get started faster. I would like to do a new website (lets call it "blg-www"), hence, many things need to change.
   Just a bit of background for you:
     blg-wiki was developed for the purpose of detailed documentation, user guide.
     blg-www is a new hugo cms, that we are now working, to develop our new website for https://bigledger.com (we would like to forward the https://www.bigledger.com to https://bigledger.com as well)
     Previously, we host our https://bigledger.com with WpEngine.com , a wordpress website hosting provider. But we are no longer paying them, and the website is currently down.
   first of all, the blg-www is currently hosted at WP Engine, and i have stopped paying recently, and the wordpress server is shutdown. But I have not setup the b
lg-www yet. Let me share with you the following information:

   * My godaddy api credentials is stored in the following home directory : ~/.aimatrix/credentials/godaddy.txt
   * if you look at ~/.aws/credentials file, there are 2 profiles, [web-publisher] and [admin@aimatrix.com] both will have access to the aws cloud account, to conf
igure the ACM certificate, aws cloud front, s3 buckets etc. 

 * For each of the task below, you can use several sub-agents to work on them


2) Tips
   As I have initialized this folder, by "forking" from the blg-wiki to blg-www , and I haven't setup the cloudfront, the ACM certificate, the Godaddy DNS server configurations yet, so, we may have to do these setup and configurations.
   As we forked from blg-wiki to blg-www, i don't want you to screw up, so all the github actions, and codes that push to the remote, configurations need to be inspected in detailed, to make sure nothing screw up. 
   For the configurations of the blg-www , you can take a peek at the other websites i have configured in the AWS cloudfront s3, for example docs.aimatrix.com , wiki.bigledger.com etc... (please ensure you don't mix them together , don't screw up, i am just asking you to see only)

3) Our priorities as follow:
  a) Get the website https://bigledger.com up and running first, even with the content from the blg-wiki is NOT suitable to be for the company home page.
     - This means, you need to configure a new s3 bucket, for the blg-www , configure the acm certificate, update the godaddy DNS record, and update the cloud front, and perform the testing for this.
  b) Next, simplify the website, we will still use hugo cms, we will remove the contents that are "not ready", and we just make the website simple, straight forward, and remove all the detailed contents of the wiki (applet), but before you remove, you can get the information from it, so that you can summarize and present this information in the blg-www. 


* Please make use of multiple sub-agents to execute this in parallel.




