library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(

  # Application title
  titlePanel("Predict Energy Use"),

  # Sidebar with a slider input for the number of bins
  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Number of bins:",
                  min = 1,
                  max = 50,
                  value = 30),
    sidebarPanel(
      selectInput("state_factor", "Building State",
                  c("State_1", "State_2", "State_4", 
                    "State_6","State_8","State_10",
                    "State_11"))
    )),
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("distPlot")
    )
  )
))

