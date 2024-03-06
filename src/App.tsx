import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState<any>()
  const [token] = useState<any>("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6IkFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.so9KYHiZLO3r1_lFgwA3v-7kQDtls54_93tO3AmKkqQ")
  const [pdf, setPdf] = useState<any>()
  const [blogsss, setBlogsss] = useState<any>()
  const getblogs = async()=>{
    const {data} = await axios.get("http://localhost:1200/_api/blogs",{
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    console.log(data);
    
    setBlogsss(data)
  }
  useEffect(()=>{
    getblogs()
  },[])
  const Data = async () => {
    let cv = {
      'Size Range': 'DN330 to DN 400',
      'Pressure Rating': 'PN6 to PN25',
      'End Connection Type': 'Flanged, Buttweld End, Socketweld End, Screwed',
      'Material Of Construction': `GM BS1400 LG4C / NAB NES747 PARTII / Bronze (RG5) / ASTM A216 Gr. WCB / ASTM A351 Gr.CF8/ASTM A351 Gr.CF8M/ASTM A351 Gr.CF3 /Cast Iron/Nodular Cast Iron/Ductile Iron`
    }
    let form = new FormData();
    form.append("image", count)
    // form.append("image", pdf)
    form.append("dataOfValues", JSON.stringify(cv))
    form.append("name", "Simple Type Strainer")
    form.append("type", "strainer")
    form.append("category", "strainer")
    form.append("blogID", "1d27e3b6-f50c-43b8-a4be-cd95af45c5c7")
    form.append("title", "d97c752a-7926-4837-86bf-2c435dcbceb6")
    form.append("htmlContent", "d97c752a-7926-4837-86bf-2c435dcbceb6")
    form.append("author", "d97c752a-7926-4837-86bf-2c435dcbceb6")
    form.append("tags", JSON.stringify(['asdasd','cxce']))
    const { data } = await axios.put("http://localhost:1200/_api/blogs", form, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    console.log(data);
  }
  const handleImageChange = (event: any) => {
    const file = event.target.files[0];
    setCount(file);
  };
  const handlePDFChange = (e: any) => {
    const file = e.target.files[0];
    setPdf(file);
  }

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
        <input type='file' onChange={handleImageChange} />
        <h1>sdhfhdg</h1>
        <input type='file' onChange={handlePDFChange} />
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <div>
        { blogsss ? blogsss.map((value:any)=>{
          return(
            <div>
              <h1>{value.id}</h1>
              {/* <h1>{value.id}</h1>
              <h1>{value.id}</h1> */}
              <img src={`http://localhost:1200${value['iamge url']}`} />
            </div>
          )
        }):<h1>dvfdavf</h1>}
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <button onClick={Data}>Submit</button>
    </>
  )
}

export default App
