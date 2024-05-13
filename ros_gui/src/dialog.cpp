#include "dialog.h"
#include "ui_dialog.h"
#include <QDebug>
#include <QDateTime>

Dialog::Dialog(QWidget *parent) :
  QDialog(parent),
  ui(new Ui::Dialog)
{
  ui->setupUi(this);
  nh_.reset(new ros::NodeHandle("~"));
  ros_timer = new QTimer(this);
  connect(ros_timer, SIGNAL(timeout()), this, SLOT(spinOnce()));
  ros_timer->start(100);

  std::int8_t order_topic;
  order_pub_ = nh_->advertise<std_msgs::Int8>("order_topic",1);

  timer = new QTimer(this);
  connect(timer, SIGNAL(timeout()),this,SLOT(timerfunc()));
  timer->start(1000);
  showFullScreen();
  QPixmap bkgrnd2("/home/mokhaled/ros_ws/src/robotics.jpeg");
  //bkgrnd = bkgrnd.scaled(this->size(), Qt::IgnoreAspectRatio);
  bkgrnd2 = bkgrnd2.scaled(1900,1080);
  QPalette palette2;
  palette2.setBrush(QPalette::Window, bkgrnd2);
  this->setPalette(palette2);





  // Dialog wind;
  // wind.show();

  QPixmap pixmap("/home/mokhaled/ros_ws/src/wave.png");
  QIcon ButtonIcon(pixmap);
  ui->hello->setIcon(ButtonIcon);
  ui->hello->setIconSize(pixmap.rect().size());

  QPixmap pixmap2("/home/mokhaled/ros_ws/src/close.png");
  QIcon ButtonIcon2(pixmap2);
  ui->close->setIcon(ButtonIcon2);
  ui->close->setIconSize(pixmap2.rect().size());

  QPixmap pixmap3("/home/mokhaled/ros_ws/src/gear.png");
  QIcon ButtonIcon3(pixmap3);
  ui->settings->setIcon(ButtonIcon3);
  ui->settings->setIconSize(pixmap3.rect().size());

  QPixmap pixmap4("/home/mokhaled/ros_ws/src/candy.png");
  QIcon ButtonIcon4(pixmap4);
  ui->pushButton_5->setIcon(ButtonIcon4);
  ui->pushButton_5->setIconSize(pixmap4.rect().size());

  ui->hello->setFlat(true);
  ui->close->setFlat(true);
  ui->settings->setFlat(true);
  ui->pushButton_5->setFlat(true);

}

Dialog::~Dialog()
{
  delete ui;
}

void Dialog::timerfunc()
{
  QTime time = QTime::currentTime();
  QString time_text = time.toString("hh : mm");
  ui->time_label->setText(time_text);
  //ui->digclock->display(time_text);
}
void Dialog::spinOnce(){
  if (ros::ok()){
    ros::spinOnce();
  }
  else
    QApplication::quit();
}



void Dialog::on_close_clicked()
{
  close();
}


void Dialog::on_hello_clicked()
{
  std_msgs::Int8 num;
  num.data = 1;
  order_pub_.publish(num);
}


void Dialog::on_pushButton_5_clicked()
{
  std_msgs::Int8 num2;
  num2.data = 2;
  order_pub_.publish(num2);
}

