import React, { useState } from 'react'

const Form = () => {
const [formData,setFormData]=useState({
  firstName:'',
  state:'',
  gender:'',
  

})
const handler=(event,field)=>{
setFormData({...formData,[field]:event.target.value})
}

  return (
    <div>
     <div className="container">
     {JSON.stringify(formData)}
  <form className="well form-horizontal" action=" " method="post" id="contact_form">
    <fieldset>
      {/* Form Name */}
      <legend>Contact Us Today!</legend>
      {/* Text input*/}
      <div className="form-group">
        <label className="col-md-4 control-label">First Name</label>  
        <div className="col-md-4 inputGroupContainer">
          <div className="input-group">
            <span className="input-group-addon"><i className="glyphicon glyphicon-user" /></span>
            <input name="firsame" onChange={(e)=>handler(e,"firstName")} value={formData.firstName} placeholder="First Name" className="form-control" type="text" />
          </div>
        </div>
      </div>
     
     
      
      {/* Select Basic */}
      <div className="form-group"> 
        <label className="col-md-4 control-label">State</label>
        <div className="col-md-4 selectContainer">
          <div className="input-group">
            <span className="input-group-addon"><i className="glyphicon glyphicon-list" /></span>
            <select name="state" onChange={e=>handler(e,"state")} value={formData.state} className="form-control selectpicker">
              <option value=" ">Please select your state</option>
              <option>Alabama</option>
              <option>Alaska</option>
              <option>Arizona</option>
              <option>Arkansas</option>
              <option>California</option>
              <option>Colorado</option>
             
            </select>
          </div>
        </div>
      </div>
     
    
      {/* radio checks */}
      <div className="form-group">
        <label className="col-md-4 control-label">Select Gender:</label>
        <div className="col-md-4">
          <div className="radio">
            <label>
              <input type="radio" name="gender" value="male"  onChange={e=>handler(e,"hosting")}/> male
            </label>
          </div>
          <div className="radio">
            <label>
              <input type="radio" name="gender"  value="female" onChange={e=>handler(e,"hosting")} /> female
            </label>
          </div>
        </div>
      </div>
    
    </fieldset>
  </form>
</div>

    </div>
  )
}

export default Form
