#include "ros_gui.h"
#include "ui_rosgui.h"
#include <QWidget>

RosGUI::RosGUI(QWidget *parent) :
  QWidget(parent),
  ui(new Ui::RosGUI)
{
  ui->setupUi(this);
  /*
  nh_.reset(new ros::NodeHandle("~"));
  ros_timer = new QTimer(this);
  connect(ros_timer, SIGNAL(timeout()), this, SLOT(spinOnce()));
  ros_timer->start(100);*/
  QPixmap bkgrnd("/home/mokhaled/ros_ws/src/smiley.jpg");
  //bkgrnd = bkgrnd.scaled(this->size(), Qt::IgnoreAspectRatio);
  bkgrnd = bkgrnd.scaled(1900,1080);
  QPalette palette;
  palette.setBrush(QPalette::Window, bkgrnd);
  this->setPalette(palette);

  ui->pushButton->setFlat(true);
  ui->pushButton_2->setFlat(true);





  // QTimer *timer = new QTimer(this);
  // connect(timer, &QTimer::timeout, this, &RosGUI::showTime);
  // timer->start(1000);
  showFullScreen();

  // showTime();

  // timer = new QTimer(this);
  // connect(timer, SIGNAL(timeout()),this,SLOT(timerfunc()));
  // timer->start(1000);


}

RosGUI::~RosGUI()
{
  delete ui;
}

/*void RosGUI::spinOnce(){
  if (ros::ok()){
    ros::spinOnce();
  }
  else
    QApplication::quit();
}

*/
// void RosGUI::showTime()
// {
//     QTime time = QTime::currentTime();
//     QString text = time.toString("HH:MM");
//     if ((time.second() % 2) == 0)
//         text[2] = ' ';
//     //ui->clock->display(text);
// }



void RosGUI::on_pushButton_clicked()
{
  // Dialog secdialog;
  // secdialog.setModal(true);
  // secdialog.exec();
  secdialog = new Dialog(this);
  secdialog->show();
  //hide();

}


void RosGUI::on_pushButton_2_clicked()
{
  close();
}

