var React = require("react");
var TodoForm = require('./TodoForm');
var TodoTable = require('./TodoTable');


var Todo = React.createClass({
    getInitialState : function () {
       return{
           todos : []
       }
    },
    listTodo : function () {
        $.ajax({
            type : 'get',
            url : '/list'
        }).done(function(resp){
            if(resp.status == "success"){
                this.setState({todos:resp.todos});
            }
        }.bind(this))
    },
    addTodo : function(content){
        $.ajax({
            type : 'post',
            url : 'add',
            data : {content:content}
        }).done(function (resp) {
            if(resp.status == "success"){
                this.listTodo();
            }
        }.bind(this))
    },
    updateTodo : function(id,status){
        $.ajax({
            type : 'post',
            url : 'update',
            data : {id:id,status:status}
        }).done(function (resp) {
            if(resp.status == "success"){
                this.listTodo();
            }
        }.bind(this))
    },
    deleteTodo : function(id){
         $.ajax({
            type : 'get',
            url : '/delete/'+id
        }).done(function(resp){
            console.log(resp);
            if(resp.status == 'success'){
                this.listTodo();
            }
        }.bind(this))

    },
    componentDidMount : function(){
        this.listTodo();
    },
    render : function(){

        return(
            <div>
                <TodoForm addTodo = {this.addTodo} />
                <TodoTable todos = {this.state.todos} updateTodo={this.updateTodo} deleteTodo = {this.deleteTodo}/>
            </div>
        )
    }
});

module.exports = Todo;
