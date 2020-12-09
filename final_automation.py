#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import getpass
import subprocess
import pyttsx3
while(True):
    def aws_menu():	
        os.system('cls')
        os.system('tput setaf 3')
        print("") 
        print("\t\t\t\t\tFOR AWS CONFIGURATION: ")
        os.system('tput setaf 5')
        print("PLEASE ENTER YOUR\n 1. IAM ACCESS KEY ID \n 2. ACCESS KEY \n 3. REGION \n 4. OUTPUT FORMAT \n ") 
        os.system("aws configure")
        print("\n\n \t\t\t\tAWS CONFIGURED!!")
        os.system("color 02")
        input("\n\nenter to continue............")
        while(True): 
            def ec2_menu():
                while(True):

                    os.system('cls')
                    os.system('tput setaf 7')
                    print("\t\t\t\tWELCOME TO EC-2 SERVICE !!")
                    print("\t\t\t\t**************************")
                    os.system('tput setaf 6')
                    print("""
                            PRESS 1:TO LAUNCH YOUR INSTANCE
                            PRESS 2:TO START YOUR INSTANCE
                            PRESS 3:To STOP YOUR INSTANCE
                            PRESS 4:TO DESCRIBE YOUR INSTANCES
                            PRESS 5:RETURN TO MAIN MENU
                            PRESS 6:TO EXIT
                            """)
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        count=int(input("How many instance you want to launch:"))
                        ami= input("Enter the image id of the instance:- ")
                        subnet_id = input("Enter the subnet id : ")
                        instance_type= input("Enter the type of instance that you want to launch :")
                        key_name = input("Enter your keyname:")
                        os.system("aws ec2 run-instances  --image-id {ami} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --key-name {key_name} ")
                        print("\n\n\t\t Your Instance Launched!")
                        print("")
                        input("\n Enter to continue..............")
                    elif choice == "2":
                        instanceid = input("Enter your instance id :")
                        os.system("aws ec2 start-instances --instance-ids {}".format(instanceid))
                        input("\n Enter to continue..............")
                    elif choice == "3":
                        instanceid = input("Enter your instance id :")
                        os.system("aws ec2 stop-instances --instance-ids {}".format(instanceid))
                        input("\n Enter to continue..............")
                    elif choice == "4":
                        os.system("color 02")
                        os.system("aws ec2 describe-instances")
                        input("\n\n Enter to continue..............")
                    elif choice == "5":
                        return
                    else:
                        os.system('tput setaf 7')
                        exit()
            def key_pair_menu():
                while True:
                    os.system('cls')
                    os.system('tput setaf 7')
                    print("\t\t\t\t\t\t\tAWS KEY PAIR MENU ")
                    print("\t\t\t\t\t\t\t*******************")
                    os.system('tput setaf 6')
                    print("""
                                PRESS 1: TO CREATE KEY-PAIR
                                PRESS 2: TO DELETE KEY-PAIR
                                PRESS 3: TO DESCRIBE KEY-PAIR
                                PRESS 4: TO EXIT
                            """)
                    choice = input(" Enter your choice : ")
                    if choice == "1":
                        key_name = input("Enter Key-name: ")
                        os.system("aws ec2 create-key-pair --key-name {} --query KeyMaterial --output text >  {}".format(key_name,key_name))
                        input("\n Enter to continue..............")
                    elif choice == "2":
                        key_name = input("Enter Key-name")
                        os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
                        input("\n Enter to continue..............")
                    elif choice == "3":
                        os.system("color 02")
                        os.system("aws ec2 describe-key-pairs")
                        input("\n Enter to continue..............")
                    else:
                        os.system('tput setaf 1')
                        print("You have typed something wrong!")
                        input("ARE YOU SURE YOU WANT TO EXIT!! \n Enter to continue..............")
                        return
            def security_Group_menu():
                while(True):
                    os.system('cls')
                    os.system('tput setaf 7')
                    print("\t\t\t\t\tWELCOME TO SECURITY GROUP MENU ")
                    print("\t\t\t\t\t*******************************")
                    os.system('tput setaf 3')
                    print("""
                            PRESS 1: TO CREATE SECURITY GROUP
                            PRESS 2: TO DELETE SECURITY GROUP
                            PRESS 3: TO DESCRIBE SECURITY GROUP
                            PRESS 4: TO EXIT
                        """)
                    choice = int(input("Enter your choice:"))
                    if choice == 1:
                        os.system("color 02")
                        des = input("Enter Description of security group : ")
                        gn = input("Enter security group Name : ")
                        os.system("aws ec2  create-security-group --description {des} --group-name {gn}")
                        input("\n Enter to continue..............")
                    elif choice == 2:
                        os.system("color 02")
                        id = input("Enter secirity group Id: ")
                        os.system(" aws ec2 delete-security-group --group-id {id}")
                    elif choice == 3:
                        os.system("color 02")
                        os.system("aws ec2 describe-security-groups")
                        input("\n Enter to continue..............")
                    else:
                        os.system('cls')
                        return            
            def ebs_menu():
                while(True):
                    os.system('cls')
                    os.system('tput setaf 7')
                    print("\t\t\t\t\tAWS VOLUME MENU ")
                    print("\t\t\t\t\t****************")
                    os.system('tput setaf 5')
                    print("""
                            PRESS 1: TO CREATE VOLUME
                            PRESS 2: TO DELETE VOLUME
                            PRESS 3: TO ATTACH VOLUME
                            PRESS 4: TO DETACH VOLUME
                            PRESS 5: TO DESCRIBE VOLUME
                            PRESS 6: TO RETURN TO MAIN MENU
                        """)
                    choice=input("Enter your Choice: ") 
                    if choice == "1":
                        zone = input("Enter AZ : ")
                        size = input("size: ")
                        os.system("aws ec2 create-volume --availability-zone {} --size {}".format(zone,size))
                        input("\n Enter to continue..............")
                    elif choice == "2":
                        volume_id = input("Enter Volume ID : ")
                        os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
                        input("\n Enter to continue..............")
                    elif choice == "3":
                        device_name = input("Enter  device Name: ")
                        instance_id = input("Instance ID: ")
                        volume_id = input("Volume ID: ")
                        os.system("aws ec2 attach-volume --device {device_name} --instance-id {instance_id} --volume-id {volume_id} ")
                        input("\n Enter to continue..............")
                    elif choice == "4":
                        volume_id = input("Volume ID: ")
                        os.system("aws ec2 detach-volume --volume-id {} ".format(volume_id))
                        input("\n Enter to continue..............")
                    elif choice == "5":
                        os.system("color 02")
                        os.system("aws ec2 describe-volumes")
                        input("\n Enter to continue..............")
                    else:
                        os.system('tput setaf 7')
                        return
            def s3_menu():
                while(True):
                    os.system("cls")
                    os.system('tput setaf 7')
                    print("\t\t\t\tWELCOME TO S3 SERVICE !!")
                    print("\t\t\t\t************************")
                    os.system('tput setaf 4')
                    print('''
                            Press 1: FOR CREATING BUCKET
                            Press 2: FOR ADDING OBJECT(IMAGE/VIDEOS)
                            Press 3: FOR BUCKET LIST
                            Press 4: FOR DELETING BUCKET
                            Press 5: FOR DELETING OBJECT OF BUCKET
                            PRESS 6: TO RETURN TO MAIN MENU
                        ''')
                    choice=input("Enter your choice :")
                    if choice == "1":
                        bucket_name=input("ENTER BUCKET NAME: ")
                        region=input("ENTER REGION: ")
                        os.system(" aws s3api create-bucket --bucket {bucket_name}  --region {region} --create-bucket-configuration  LocationConstraint={region}")
                        input("\n Enter to continue..............")
                    elif choice == "2":
                        bucket_name=input("\n ENTER BUCKET NAME: ")
                        obj_path= input("\t ENTER THE PATH OF THE OBJECT:")
                        name=input("ENTER THE NAME OF THE OBJECT:")
                        os.system("aws s3api put-object --bucket {bucket_name} --key {name} --body \"{obj_path}\"")
                        input("ENTER TO CONTINUE.........")
                    elif choice == "3":
                        os.system('aws s3api list-buckets --query "Buckets[].Name"')
                        input("\n Enter to continue..............")
                    elif choice == "4":
                        bucket_name=input("\n ENTER BUCKET NAME: ")
                        region_name=input("\n ENTER REGION:")
                        os.system("aws s3api delete-bucket --bucket {bucket_name} --region {region_name}")
                    elif choice == "5":
                        bucket_name=input("\n ENTER BUCKET NAME: ")
                        object_name=input("\n ENTER OBJECT NAME: ")
                        os.system("aws s3 rm s3://{bucket}/{object}".format(bucket=bucket_name,object=object_name))
                        input("\n Enter to continue..............")
                    else:
                        return           
            def cloudFront_menu():
                while(True):
                    os.system("cls")
                    os.system('tput setaf 10')
                    print("\t\t\t\t\t\t WELCOME TO CLOUD FRONT DISTRIBUTION ")
                    print("\t\t\t\t\t\t*************************************")
                    os.system('tput setaf 6')
                    print('For creating cloud front distribution;Enter some required details')
                    bucketname=input("\nENTER BUCKET NAME:")
                    objectname=input("\nENTER OBJECT NAME:")
                    os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucketname,objectname))
                    input("ENTER TO CONTINUE..............")
            os.system('clear')
            os.system('tput setaf 7')
            print("\t\t\t\t\t\t\tAWS MENU DRIVEN ")
            print("\t\t\t\t\t\t\t****************")
            os.system('tput setaf 6')
            print("""
                    Press 1: FOR CREATING YOUR KEY PAIR
                    Press 2: FOR SECURITY-GROUP SERVICES	
                    Press 3: FOR EC2 SERVICES
                    Press 4: FOR EBS SERVICES
                    Press 5: FOR S3 SERVICES
                    Press 6: FOR CLOUD FRONT DISTRIBUTION SERVICES
                    Press 7: FOR RETURNING TO MAIN MENU
                """)
            choice = int(input("\n Enter Your Choice:\t"))
            if choice == 1:
                key_pair_menu()
            elif choice == 2:
                security_Group_menu()
            elif choice == 3:
                ec2_menu()
            elif choice == 4:
                ebs_menu()
            elif choice == 5:
                s3_menu()
            elif choice == 6:
                cloudFront_menu()
            else:
                return
    def docker_menu():
        print("""
                   Press 1. Configure webserver inside docker container
                   Press 2. Run python code bt stting up the python interpreter inside docker container
              """)
        choice=int(input("Enter your choice : "))
        if choice==1:
            os.system("systemctl start docker")
            os.system("docker create -it --network host --name task72os centos")
            os.system("docker start task72os")
            os.system("docker exec -it task72os yum clean all")
            os.system("docker exec -it task72os yum install httpd -y")
            os.system("docker exec -it task72os yum install net-tools wget -y")
            os.system("docker exec -it task72os wget -O /var/www/html/a.html https://task7arth.s3.ap-south-1.amazonaws.com/a.html") 
            os.system("docker exec -it task72os /usr/sbin/httpd")
            os.system("docker exec -it task72os ifconfig docker0")
        elif choice==2:
            os.system("systemctl start docker")
            os.system("docker create -it --network host --name task72os2 centos")
            os.system("docker start task72os2")
            os.system("docker exec -it task72os2 yum clean all")
            os.system("docker exec -it task72os2 yum install python3 wget -y")
            os.system("docker exec -it task72os2 wget -O /a.py https://task7arth.s3.ap-south-1.amazonaws.com/a.py")
            os.system("docker exec -it task72os2 python3 a.py")
        else:
            print("Invalid choice")
    
    def hadoop_menu():
        os.system("clear")
        os.system('tput setaf 7')
        print("\t\t\tWELCOME TO THE WORLD OF HADOOP !!")
        print("\t\t\t=================================")
        while True:
            os.system('tput setaf 2')
            print("""
                        PRESS 1: TO INSTALL HADOOP & JAVA
                        PRESS 2: TO CONFIGURE DATA NODE & NAME NODE
                        PRESS 3: TO FORMAT NAME NODE
                        PRESS 4: TO START HADOOP SERVICES
                        PRESS 5: TO STOP HADOOP SERVICES
                        PRESS 6: TO GET HADOOP REPORTS
                        PRESS 8: TO RETURN TO THE MAIN MENU
                    """)
            choice = input("Enter your choice: ")
            if choice == "1":
                os.system("rpm -ihv  jdk-8u171-linux-x64.rpm")
                os.system("rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force")
            elif choice == "2":
                os.system("vim /etc/hadoop/hdfs-site.xml")
                os.system("vim /etc/hadoop/core-site.xml")
            elif choice == '3':
                os.system("hadoop namenode -format")
                input("Enter to continue.....")
            elif choice == "4":
                node = input("""
                              PRESS 1: FOR STARTING NAMENODE
                              PRESS 2: FOR DELETING DATANODE
                                        """)
                if node == "1":
                    os.system("hadoop-daemon.sh start namenode")
                    input("Enter to continue.....")
                elif node == "2":
                    os.system("hadoop-daemon.sh start datanode")
                    input("Enter to continue.....")
                else:
                    print("wrong choice!!! :( ")
                    return
            elif choice == 5:
                stopnode = input("""
                                 PRESS 1: FOR STOPPING NAMENODE
                                 PRESS 2: FOR STOPPING DATANODE
                                        """)
                if stopnode == "1":
                    os.system("hadoop-daemon.sh stop namenode")
                    input("Enter to continue.....")
                elif stopnode == "2":
                    os.system("hadoop-daemon.sh stop datanode")
                    input("Enter to continue.....")
                else:
                    print("WRONG CHOICE ! :( ")
                    return
            elif choice == "6":
                os.system("hadoop dfsasdmin -report")
                input("Enter to continue.....")
            else:
                input("Enter to continue.....")
                return
    def lvm_menu():
        os.system('clear')
        os.system('tput setaf 7')
        print("")
        print("\t\t\t\t LOGICAL VOLUME MANAGEMENT MENU")
        print("\t\t\t\t********************************")
        os.system("tput setaf 4")
        print("""
                PRESS 1:TO CHECK TOTAL DISK
                PRESS 2:TO CREATE PHYSICAL VOLUME
                PRESS 3:TO DISPLAY PHYSICAL VOLUME
                PRESS 4:TO CREATE VOLUME GROUP
                PRESS 5:TO DISPLAY VOLUME GROUP
                PRESS 6:TO CREATE LOGICAL VOLUME
                PRESS 7:TO DISPLAY LOGICAL VOLUME
                PRESS 8:TO EXTEND SIZE OF LOGICAL VOLUME
                PRESS 9:TO FORMAT THE PARTITION
                PRESS 10:TO ATTACH ONE MORE HARD DISK
                PRESS 11:TO RETURN TO MAIN MENU
                PRESS 12:TO EXIT
                """)
        
        d = int(input("Enter the choice : "))
        if d == 1:
                os.system('tput setaf 2')
                os.system("fdisk -l")
                input("Enter to continue..........")
        elif d == 2:
                hd1 = input("Enter your hard disk 1 name: ")
                hd2 = input("Enter your hard disk 2 name: ")
                os.system("pvcreate /dev/"+hd1)
                os.system("pvcreate /dev/"+hd2)
                input("Enter to continue..........")
        elif d == 3:
                pv = input("Enter the name of the volume group: ")
                os.system("pvdisplay {}".format(pv))
                input("Enter to continue..........")
        elif d == 4:
                vg = input("Enter the name of the volume group: ")
                epv = input("Enter your physical volume that you have created: ")
                os.system("vgcreate "+vg+" /dev/"+epv+" /dev/"+b)
                input("Enter to continue..........")
        elif d == 5:
                vgd = input("Enter the name of the volume group: ")
                os.system("vgdisplay {}".format(vgd))
                input("Enter to continue..........")
        elif d == 6:
                vg = input("Enter the name of the volume group: ")
                size = input("Enter the size of your logical volume: ")
                lv = input("Enter the name of the logical group: ")
                os.system("lvcreate --size +"+size+"G --name "+lv+" "+vg)
                input("Enter to continue..........")
        elif d == 7:
                os.system("lvdisplay")
                input("Enter to continue..........")
        elif d == 8:
                vg1 = input("Enter the name of the volume group: ")
                lv1 = input("Enter the name of the logical volume group: ")
                os.system("mkfs.ext4 /dev/{}/{}".format(vg1,lv1))
                print("\n\n !!NOW WE WILL CREATE A DIRECTORY!!")
                drive = input("Enter the name of the drive you want to create:")
                os.system("mkdir /{}".format(drive))
                print("\nSUCCESSFULLY FORMATTED!!")
                esize = input("\nEnter the size you want to extend: ")
                lve = input("Enter the name of logical volume group : ")
                vge = input("Enter the name of the volume group: ")
                os.system("lvextend --size {} /dev/{}/{}".format(esize,vge,lve))
                print("\n\t\t\t\tEXTENTED SUCCESSFULLY!!\n")
                input("Enter to continue..........")
        elif d == 9:
                vg1 = input("Enter the name of the volume group: ")
                lve = input("Enter the name of logical volume group : ")
                os.system("resize2fs /dev/{}/{}".format(vg1,lve))
                input("Enter to continue..........")
        elif d == 10:
                hd = input("Enter the name of the hard disk: ")
                vg = input("Enter the name of the volume group: ")
                os.system("vgextend {} /dev/{}".format(vg,hd))
                input("Enter to continue..........")
        else:
                print("Wrong choice!!")
                input("Enter to continue...........")
                return

    os.system("clear")
    os.system('tput setaf 7')
    print("\t\t\t\t\tAUTOMATION OF DIFFERENT TECHNOLOGY!!")
    print("\t\t\t\t\t************************************")
    os.system('tput setaf 3')
    print("""
                Press 1:  FOR ENTERING YOUR AWS CLOUD WORLD!!
                \n
                Press 2:  FOR ENTERING DOCKER WORLD!!
                \n
                Press 3:  FOR ENTERING HADOOP WORLD!!
                \n
                Press 4:  FOR ENTERING LVM WORLD!!	   
             """)
    os.system('tput setaf 7')
    choice = int(input("\n Enter your choice:"))
    if int(choice)== 1:
        aws_menu()
    elif int(choice)==2:
        docker_menu()
    elif int(choice)== 3:
        hadoop_menu()
    elif int(choice)== 4:
        lvm_menu()
    else:
        exit()
    

# In[ ]:







   
        

