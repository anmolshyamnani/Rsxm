import type { ReactNode } from 'react';
export const metadata = { title: 'AI Operating System', description: '24×7 company, project and research command center' };
export default function RootLayout({children}:{children:ReactNode}) { return <html lang="en"><body style={{margin:0}}>{children}</body></html>; }
