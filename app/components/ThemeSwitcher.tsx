'use client';

import { useTheme } from "next-themes";
import { useEffect, useState } from "react";
import { Moon, Sun } from "iconsax-react";

export function ThemeSwitcher() {
  const [mounted, setMounted] = useState(false);
  const { theme, setTheme } = useTheme()

  useEffect(() => {
    setMounted(true)
  }, [])

  if(!mounted) return null

  return (
    <div className="flex fixed top-5 right-5 z-[99]">
      <button onClick={() => setTheme('light')} aria-label="Switch to Light Mode"
        className="p-2 rounded-full border border-slate-600 flex items-center justify-center ml-2"
        >
        <Sun size="24" color={theme === "light" ? "black" : "white"} />
      </button>
      <button onClick={() => setTheme('dark')} aria-label="Switch to Dark Mode"
        className="p-2 rounded-full border border-slate-600 flex items-center justify-center ml-2"
        >
        <Moon size={24} color={theme === 'dark' ? "white" : "black"} />
      </button>
    </div>
  );
};