import React,{Component} from 'react';
import axios from 'axios';

function App extends Component{

  constructor(props){
    super(props);
    this.state =({
      alumnos: []
    })
  }
  componentDidMount(){
    axios.get('http://localhost:5000/alumnos')
    .then(res=>{
      console.log(res.data);
      this.setState({alumnos:res.data})
    })
  }
  render() {
    return(
      <div>Hola mundo
        {
        this.state.alumnos.map(alumno => {
          return(
            <div>
              <p>{alumno.nombre}</p>
              <p>{alumno.email}</p>
            </div>
          )})
      }
    )
      </div>
      
  }
}

export default App;
