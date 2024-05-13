#ifndef ROS_GUI_H
#define ROS_GUI_H

#include <QWidget>
#include <QLCDNumber>
#include <QTime>
#include <QTimer>
#include <QDateTime>
#include "dialog.h"

#include <ros/ros.h>
#include <std_msgs/String.h>
#include <qtimer.h>
#include <sstream>

namespace Ui {
class RosGUI;
}

class RosGUI : public QWidget
{
  Q_OBJECT

public:
  explicit RosGUI(QWidget *parent = nullptr);
  ~RosGUI();
/*
public slots:
  void spinOnce();*/

private:
  Ui::RosGUI *ui;
  QTimer *timer;
  Dialog *secdialog;


public slots:
  /*
  QTimer *ros_timer;
  ros::NodeHandlePtr nh_;
  ros::Subscriber chatter_sub_;*/
private slots:
  void on_pushButton_clicked();
  void on_pushButton_2_clicked();
};



#endif // ROS_GUI_H
