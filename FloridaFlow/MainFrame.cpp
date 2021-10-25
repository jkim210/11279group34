#include "MainFrame.h"
#include "Algorithm.h"
#include <wx/splitter.h>

enum
{
    ID_Hello = 1
};

MainFrame::MainFrame() : wxFrame(NULL, wxID_ANY, "Florida Flow", wxPoint(100, 100), wxSize(1200, 800))
{

    // Stuff for top menu bar

    wxMenu *menuFile = new wxMenu;
    menuFile->Append(ID_Hello, "&Hello...\tCtrl-H",
                     "Help string shown in status bar for this menu item");
    menuFile->AppendSeparator();
    menuFile->Append(wxID_EXIT);

    wxMenu *menuHelp = new wxMenu;
    menuHelp->Append(wxID_ABOUT);

    wxMenuBar *menuBar = new wxMenuBar;
    menuBar->Append(menuFile, "&File");
    menuBar->Append(menuHelp, "&Help");

    SetMenuBar(menuBar);

    CreateStatusBar();
    SetStatusText("Select highlight tool to highlight map");

    Bind(wxEVT_MENU, &MainFrame::OnHello, this, ID_Hello);
    Bind(wxEVT_MENU, &MainFrame::OnAbout, this, wxID_ABOUT);
    Bind(wxEVT_MENU, &MainFrame::OnExit, this, wxID_EXIT);

    // Split screen for UI and map

    /*wxSplitterWindow *splitter = new wxSplitterWindow(this);
    wxPanel *left = new wxPanel(splitter);
    wxPanel *right = new wxPanel(splitter);

    left->SetBackgroundColour(wxColor(100, 100, 200));
    right->SetOwnBackgroundColour(wxColor(200, 100, 200));

    splitter->SplitVertically(left, right);*/

    wxBoxSizer *sizer = new wxBoxSizer(wxVERTICAL);

    generate = new wxButton(this, BUTTON_generate, "RUN SIMULATION");

    sizer->Add(generate, 40,0, 0);

    sizer->SetSizeHints(this);
    SetSizer(sizer);


}

// Runs when application is quit
void MainFrame::OnExit(wxCommandEvent& event)
{
    Close(true);
}

// Displays text when clicking wxWidgets -> about in upper left hand corner of screen (at least on mac)
void MainFrame::OnAbout(wxCommandEvent& event)
{
    wxMessageBox("(c) 2021 Waterbenders",
                 "About Florida Flow", wxOK | wxICON_INFORMATION);
}
void MainFrame::OnHello(wxCommandEvent& event)
{
    wxLogMessage("Hello world from wxWidgets!");
}

BEGIN_EVENT_TABLE(MainFrame, wxFrame)
EVT_BUTTON(BUTTON_generate, MainFrame::OnExit) // TODO Change function
END_EVENT_TABLE()