# Question: AWS Architecture

Novozymes leverages AWS Cloud to build and deploy its internal and external software.
Below, please explain how you would deploy a full-stack single page application (database, backend, frontend) with the ability to send notifications to users via email, on AWS and why you chose the infrastructure you did.
The requirements for this full-stack web application are:

- It must be scalable for an increase or decrease in the number of active users
- It follows AWS recommended security guidelines
- Do not address language or framework of frontend or backend
- Any database technology is acceptable and do not discuss pros and cons of the database choice - Assume DNS and SSL certificate configuration are already in place

At a minimum describe each of the AWS resources that you would use, how they are connected, and the security considerations for each.

## Answer

The AWS resources I would use to build a SPA are:

1. Route 53 - Set up the domain and hosted zone

2. Simple Storage Service (S3) - Create a bucket to host all files for the SPA, turn on static hosting, and configure the bucket policy

3. CloudFront - Utilize as a content delivery network (CDN) from our S3, redirect HTTP to HTTPS, and redirect error responses to index.html to allow the SPA handle routing

4. Simple Notification Service (SNS) - To create subscription with CloudWatch as publisher when events occur in CodeBuild and the protocol set to email. Use DLQs to handle undeliverable emails.

5. CodePipeline, CodeBuild & GitHub - Orchestrate the build process of 2 branches (one for development and the other for production). GitHub will serve as the repository, CodePipeline will manage the build, and finally CodeBuild will build the code and deploy it to S3.
