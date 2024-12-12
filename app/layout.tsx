import type { Metadata } from "next";
import "./globals.css";
import { ThemeSwitcher } from "./components/ThemeSwitcher";
import { Providers } from "./providers";

// const geistSans = Geist({
//   variable: "--font-geist-sans",
//   subsets: ["latin"],
// });

// const geistMono = Geist_Mono({
//   variable: "--font-geist-mono",
//   subsets: ["latin"],
// });

export const metadata: Metadata = {
  title: "모고모고",
  description: "영어 모의고사 자동 변형 웹사이트",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`antialiased`}
      >
        <Providers>
          <ThemeSwitcher />
          {children}
        </Providers>
      </body>
    </html>
  );
}
