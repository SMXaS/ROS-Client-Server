#!/usr/bin/env python

from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse


import rospy

def rectangle_area_callback(req):
    print ("Returning [%s * %s = %s]"%(req.width, req.height, (req.width * req.height)))
    return RectangleAreaServiceResponse(req.width * req.height)

def rectangle_area_server():
    rospy.init_node('rectangle_area_server')
    s = rospy.Service('rectangle_area_service', RectangleAreaService, rectangle_area_callback)
    print("Ready to work")
    rospy.spin()

if __name__ == "__main__":
    rectangle_area_server()