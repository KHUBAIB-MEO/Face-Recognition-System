#import tensorflow as tf # type: ignore
#import numpy


#model = "liveness.model"
#model = tf.keras.models.load_model(model)

# #liveness check
            # img = frame[ymin:ymax, xmin:xmax]
            # img = cv2.resize(img, (32,32))
            # img = img.astype("float") / 255.0
            # img = tf.keras.preprocessing.image.img_to_array(img)
            # img = numpy.expand_dims(img, axis=0)

            # liveness = model.predict(img)
            # liveness = liveness[0].argmax()
 # cv2.putText(frame, f"Liveness: {'Real' if liveness == 0 else 'Fake'}", (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)