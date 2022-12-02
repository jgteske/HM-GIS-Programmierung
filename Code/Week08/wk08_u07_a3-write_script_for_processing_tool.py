# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessing,
    QgsFeatureSink,
    QgsProcessingException,
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterVectorLayer,
    QgsProcessingParameterFeatureSink,
)
from qgis import processing


class ExampleAlgo(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = "INPUT"
    OUTPUT = "OUTPUT"

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate("Processing", string)

    def createInstance(self):
        return ExampleAlgo()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return "ex_script"

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr("Example script")

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr("Example scripts")

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return "examplescripts"

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Example algorithm short description")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                "input", "INPUT", types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                "output", "OUTPUT", type=QgsProcessing.TypeVectorPolygon
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        from qgis.processing import alg
        from qgis.core import QgsCoordinateReferenceSystem
        from qgis.core import QgsProcessing
        import processing

        @alg(
            name="ex_new",
            label=alg.tr("Example script w decorators"),
            group="examplescripts",
            group_label=alg.tr("Example Scripts"),
        )
        # 'INPUT' is the recommended name for the main input parameter

        @alg.input(type=alg.SOURCE, name="INPUT", label="Input layer")
        # 'OUTPUT' is the recommended name for the main output parameter
        @alg.input(type=alg.SINK, name="OUTPUT", label="Output layer")
        # For more decorators check https://docs.qgis.org/latest/en/docs/user_manual/processing/scripts.html#the-alg-decorator
        def testalg(instance, parameters, context, feedback, inputs):
            """
            Description goes here. (Don't delete this! Removing this comment will cause errors.)
            """
            outputs = {}
            # Reproject layer
            alg_params = {
                "INPUT": parameters["INPUT"],
                "OPERATION": "",
                "TARGET_CRS": QgsCoordinateReferenceSystem("EPSG:31287"),
                "OUTPUT": QgsProcessing.TEMPORARY_OUTPUT,
            }
            outputs["ReprojectLayer"] = processing.run(
                "native:reprojectlayer",
                alg_params,
                context=context,
                feedback=feedback,
                is_child_algorithm=True,
            )

            # Buffer
            alg_params = {
                "DISSOLVE": False,
                "DISTANCE": 10000,
                "END_CAP_STYLE": 0,  # Round
                "INPUT": outputs["ReprojectLayer"]["OUTPUT"],
                "JOIN_STYLE": 0,  # Round
                "MITER_LIMIT": 2,
                "SEGMENTS": 5,
                "OUTPUT": parameters["OUTPUT"],
            }
            outputs["Buffer"] = processing.run(
                "native:buffer",
                alg_params,
                context=context,
                feedback=feedback,
                is_child_algorithm=True,
            )
            return {"OUTPUT": outputs["Buffer"]["OUTPUT"]}
