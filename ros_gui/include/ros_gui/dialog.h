#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>
#include <QTimer>
#include <QLCDNumber>
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Int8.h>
#include <qtimer.h>
#include <sstream>

namespace Ui {
class Dialog;
}

class Dialog : public QDialog
{
  Q_OBJECT

public:
  explicit Dialog(QWidget *parent = nullptr);
  ~Dialog();
public slots:
  void timerfunc();
  void spinOnce();

private slots:
  void on_close_clicked();

  void on_hello_clicked();

  void on_pushButton_5_clicked();

private:
  Ui::Dialog *ui;
  QTimer *timer;
  QTimer *ros_timer;
  ros::NodeHandlePtr nh_;
  ros::Publisher order_pub_;
};

#endif // DIALOG_H
