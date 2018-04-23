A small document
=================

Yo

Welcome. This is the first paragraph.

With a bullet list:

* blah
* blah
* reblah

With activity diagram:

.. plantuml::
   :caption: Caption with **bold** and *italic*

   Bob -> Alice: hello
   Alice -> Bob: Go Away
   
We can do statecharts too:

.. plantuml::
   :caption: a statechart
   
    scale 600 width

    [*] -> State1
    State1 --> State2 : Succeeded
    State1 --> [*] : Aborted
    State2 --> State3 : Succeeded
    State2 --> [*] : Aborted
    state State3 {
      state "Accumulate Enough Data\nLong State Name" as long1
      long1 : Just a test
      [*] --> long1
      long1 --> long1 : New Data
      long1 --> ProcessData : Enough Data
    }
    State3 --> State3 : Failed
    State3 --> [*] : Succeeded / Save Result
    State3 --> [*] : Aborted
   
