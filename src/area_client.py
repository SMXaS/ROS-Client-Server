#!/usr/bin/env python

import sys
import rospy

from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

def get_rectangle_area(x, y):
    rospy.wait_for_service('rectangle_area_service')
    try:
        multiply_two_ints = rospy.ServiceProxy('rectangle_area_service', RectangleAreaService)
        response = multiply_two_ints(x, y)
        return response.area
    except rospy.ServiceException(e):
        print ("Service call failed: %s"%e)

if __name__ == "__main__":
    width = 9.1
    height = 3.5
    print ("Requesting %s*%s"%(width, height))
    area = get_rectangle_area(width, height)
    print ("%s * %s = %s"%(width, height, area))