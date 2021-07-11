#include <ros/ros.h>
#include <nav_msgs/MapMetaData.h>
#include <nav_msgs/OccupancyGrid.h>
#include <std_msgs/Header.h>


void mapCallback(const nav_msgs::OccupancyGrid::ConstPtr& msg){

    int Ngray = 0;
    int Nwhite = 0;
    int Nblack = 0;
    std_msgs::Header header = msg->header;
    nav_msgs::MapMetaData info = msg->info;
    ROS_INFO("Got map %d %d", info.width,info.height);
    for (int i = 0; i < info.height*info.width; i++){
       if (msg->data[i] == -1){
          Ngray++;
       }
       else if (msg->data[i] == 100){
           Nblack++;
       }
       else if(msg->data[i] == 0){
           Nwhite++;
       }

    }

    ROS_INFO("Number of all cells is: %d",info.width*info.height);
    ROS_INFO("Number of gray cells is: %d",Ngray);
    ROS_INFO("Number of black cells is: %d",Nblack);
    ROS_INFO("Number of white cells is: %d",Nwhite);
    printf("==========================\n");
    ROS_INFO("The cell total is: %d",Nwhite+Nblack+Ngray);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "map_reader");
    ros::NodeHandle n;

    ros::Subscriber map_sub = n.subscribe("map",2000,mapCallback);

    ros::spin();
    return 0;
}

