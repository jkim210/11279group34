#include <wx/wx.h>

class MainFrame : public wxFrame
{
public:
    MainFrame();
    wxButton* generate;
private:
    void OnHello(wxCommandEvent& event);
    void OnExit(wxCommandEvent& event);
    void OnAbout(wxCommandEvent& event);

    DECLARE_EVENT_TABLE()
};
enum
{
    BUTTON_generate = wxID_HIGHEST + 1 // declares an id which will be used to call our button
};