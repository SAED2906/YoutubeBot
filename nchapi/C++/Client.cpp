// Client.cpp : Defines the entry point for the application.
//

#include "client.h"
#include "tchar.h"
#include "windows.h"

#define MAX_LOADSTRING 100

//  Global Variables:
HINSTANCE hInst;								// current instance
TCHAR szTitle[MAX_LOADSTRING];			// The title bar text
TCHAR szWindowClass[MAX_LOADSTRING];	// the main window class name
HWND ghWnd = NULL;

// Forward declarations of functions included in this code module:
ATOM				   MyRegisterClass(HINSTANCE hInstance);
BOOL				   InitInstance(HINSTANCE, int);
LRESULT CALLBACK	WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK	About(HWND, UINT, WPARAM, LPARAM);

// test server identificator:
#define API_SERVER_KEY "APITestServer"

// constants definitions:
#define API_DLL_NAME "nchapi.dll"

// command arguments:
const unsigned int nArgs = 3;
LPCTSTR szArgs[] = {_T("-showmessagebox"),
   _T("This is the test message which should be shown\nat the message box window."),
   _T("Test message box caption.")};

// Test function
void TESTCommandSendDLL();
typedef DWORD (WINAPI *pFn) (LPCTSTR szProgramKey, UINT nArgs, LPCTSTR  const * szArgs, LPTSTR  szResultString);

int APIENTRY wWinMain(HINSTANCE hInstance,
                      HINSTANCE hPrevInstance,
                      LPTSTR    lpCmdLine,
                      int       nCmdShow)
{
	UNREFERENCED_PARAMETER(hPrevInstance);
	UNREFERENCED_PARAMETER(lpCmdLine);

 	// TODO: Place code here.
	MSG msg;
	HACCEL hAccelTable;

	// Initialize global strings
	LoadString(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
	LoadString(hInstance, IDC_CLIENT, szWindowClass, MAX_LOADSTRING);
	MyRegisterClass(hInstance);

	// Perform application initialization:
	if (!InitInstance (hInstance, nCmdShow))
	{
		return FALSE;
	}

	hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_CLIENT));

	// Main message loop:
	while (GetMessage(&msg, NULL, 0, 0))
	{
		if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
		{
			TranslateMessage(&msg);
			DispatchMessage(&msg);
		}
	}

	return (int) msg.wParam;
}



//
//  FUNCTION: MyRegisterClass()
//
//  PURPOSE: Registers the window class.
//
//  COMMENTS:
//
//    This function and its usage are only necessary if you want this code
//    to be compatible with Win32 systems prior to the 'RegisterClassEx'
//    function that was added to Windows 95. It is important to call this function
//    so that the application will get 'well formed' small icons associated
//    with it.
//
ATOM MyRegisterClass(HINSTANCE hInstance)
{
	WNDCLASSEX wcex;

	wcex.cbSize = sizeof(WNDCLASSEX);

	wcex.style		   	= CS_HREDRAW | CS_VREDRAW;
	wcex.lpfnWndProc  	= WndProc;
	wcex.cbClsExtra      = 0;
	wcex.cbWndExtra   	= 0;
	wcex.hInstance		   = hInstance;
	wcex.hIcon		   	= LoadIcon(hInstance, MAKEINTRESOURCE(IDI_CLIENT));
	wcex.hCursor	   	= LoadCursor(NULL, IDC_ARROW);
	wcex.hbrBackground	= (HBRUSH)(COLOR_WINDOW+1);
	wcex.lpszMenuName 	= MAKEINTRESOURCE(IDC_CLIENT);
	wcex.lpszClassName	= szWindowClass;
	wcex.hIconSm		   = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_CLIENT));

	return RegisterClassEx(&wcex);
}

//
//   FUNCTION: InitInstance(HINSTANCE, int)
//
//   PURPOSE: Saves instance handle and creates main window
//
//   COMMENTS:
//
//        In this function, we save the instance handle in a global variable and
//        create and display the main program window.
//
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   hInst = hInstance; // Store instance handle in our global variable

   ghWnd = CreateWindow(szWindowClass, szTitle, WS_OVERLAPPEDWINDOW,
      CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, NULL, NULL, hInstance, NULL);

   if (!ghWnd)
   {
      return FALSE;
   }

   ShowWindow(ghWnd, SW_HIDE/*nCmdShow*/);
   UpdateWindow(ghWnd);
   PostMessage(ghWnd, WM_COMMAND, MAKEWPARAM(IDM_ABOUT, 0), MAKELPARAM(0, 0));

   return TRUE;
}

//
//  FUNCTION: WndProc(HWND, UINT, WPARAM, LPARAM)
//
//  PURPOSE:  Processes messages for the main window.
//
//  WM_COMMAND	- process the application menu
//  WM_PAINT	- Paint the main window
//  WM_DESTROY	- post a quit message and return
//
//
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	int wmId, wmEvent;
	PAINTSTRUCT ps;
	HDC hdc;

	switch (message)
	{
	case WM_COMMAND:
		wmId    = LOWORD(wParam);
		wmEvent = HIWORD(wParam);
		// Parse the menu selections:
		switch (wmId)
		{
		case IDM_ABOUT:
			DialogBox(hInst, MAKEINTRESOURCE(IDD_ABOUTBOX), hWnd, About);
			break;
		case IDM_EXIT:
			DestroyWindow(hWnd);
			break;
		default:
			return DefWindowProc(hWnd, message, wParam, lParam);
		}
		break;
	case WM_PAINT:
		hdc = BeginPaint(hWnd, &ps);
		// TODO: Add any drawing code here...
		EndPaint(hWnd, &ps);
		break;
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
	default:
		return DefWindowProc(hWnd, message, wParam, lParam);
	}
	return 0;
}

// Message handler for about box.
INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
	UNREFERENCED_PARAMETER(lParam);
	switch (message) {
      case WM_INITDIALOG: {
		   return (INT_PTR)TRUE;
		   break;
      }
      case WM_COMMAND: {
		   if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL) {
			   EndDialog(hDlg, LOWORD(wParam));
            PostMessage(ghWnd, WM_COMMAND, MAKEWPARAM(IDM_EXIT, 0), MAKELPARAM(0, 0));
			   return (INT_PTR)TRUE;
		   }
         if (LOWORD(wParam) == IDC_BUTTON_TESTDLL) {
            TESTCommandSendDLL();
            return (INT_PTR)TRUE;
         }
		   break;
      }
	}
	return (INT_PTR)FALSE;
}

void TESTCommandSendDLL()
{
   // find the nchapi.dll in the same directory as the executable:
   TCHAR szDll [MAX_PATH];
   szDll[0] = 0;
   GetModuleFileName(NULL, szDll, MAX_PATH);
   // cut the full module name to module directory
   size_t i;
   for (i = _tcslen(szDll) - 1; i > 0; i--) {
      if((szDll[i] == _T('\\')) ||
         (szDll[i] == _T('/') )   ) {
         szDll[i + 1] = 0;
         break;
      }
      i--;
   }
   //add the DLL name and load it:
   _tcscat(szDll, _T(API_DLL_NAME));
   HMODULE hModDll = LoadLibrary(szDll);
   if ((hModDll == NULL) || (hModDll == INVALID_HANDLE_VALUE))
      return;
   //get the appropriate function address:
   pFn pfSendCommand = (pFn)GetProcAddress(hModDll, "NCHAPISendCommand");

   TCHAR szResultString[8096]; 
   if ((pfSendCommand)(_T(API_SERVER_KEY), nArgs, szArgs, szResultString) == 0) {
      MessageBox(NULL, szResultString, _T("Result"), MB_OK);
   } else {
      MessageBox(NULL, _T("Error: Program Not Running"), _T("Result"), MB_OK);
   }

   FreeLibrary(hModDll);
}
