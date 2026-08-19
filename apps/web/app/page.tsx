const agents = [
  ["Chief of Staff", "company"],
  ["Project Manager", "projects"],
  ["Research Agent", "research"],
  ["Literature Review", "research"],
  ["Developer Agent", "product"],
  ["Marketing Agent", "company"],
  ["Data & Analytics", "company"],
  ["Monitoring & Recovery", "system"],
];

export default function Home() {
  return (
    <main style={{minHeight:"100vh",background:"#09090b",color:"#fafafa",fontFamily:"Inter,system-ui",padding:32}}>
      <div style={{maxWidth:1280,margin:"0 auto"}}>
        <header style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:32}}>
          <div><div style={{fontSize:12,color:"#a1a1aa",letterSpacing:2}}>AI OPERATING SYSTEM</div><h1 style={{fontSize:36,margin:"8px 0"}}>Command Center</h1></div>
          <div style={{padding:"8px 12px",border:"1px solid #27272a",borderRadius:999,color:"#86efac",fontSize:13}}>● SYSTEM ONLINE</div>
        </header>
        <section style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:16,marginBottom:28}}>
          {[['Agents','8'],['Active Tasks','0'],['Projects','0'],['Approvals','0']].map(([label,value])=><div key={label} style={{background:"#111113",border:"1px solid #27272a",borderRadius:16,padding:20}}><div style={{color:"#a1a1aa",fontSize:13}}>{label}</div><div style={{fontSize:30,fontWeight:700,marginTop:8}}>{value}</div></div>)}
        </section>
        <div style={{display:"grid",gridTemplateColumns:"1.2fr .8fr",gap:20}}>
          <section style={{background:"#111113",border:"1px solid #27272a",borderRadius:16,padding:24}}>
            <h2 style={{marginTop:0}}>Agent Organization</h2>
            <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>{agents.map(([name,domain])=><div key={name} style={{border:"1px solid #27272a",borderRadius:12,padding:16}}><div style={{fontWeight:600}}>{name}</div><div style={{color:"#71717a",fontSize:12,marginTop:5}}>{domain.toUpperCase()}</div></div>)}</div>
          </section>
          <section style={{background:"#111113",border:"1px solid #27272a",borderRadius:16,padding:24}}>
            <h2 style={{marginTop:0}}>Operating Domains</h2>
            {['Company','Projects','Research','Product Development','Knowledge','Analytics','24×7 Monitoring'].map(x=><div key={x} style={{padding:"12px 0",borderBottom:"1px solid #27272a"}}>{x}</div>)}
          </section>
        </div>
      </div>
    </main>
  );
}
