library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(

  # Application title
  titlePanel("Predict Energy Use"),

  # Sidebar with a slider input for the number of bins
  sidebarLayout(
    sidebarPanel(
      sliderInput("year_built",
                  "Date of construction",
                  min = 1950,
                  max = 2010,
                  value = 1975),
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

