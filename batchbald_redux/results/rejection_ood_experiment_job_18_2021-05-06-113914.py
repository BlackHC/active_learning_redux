store = {}
store['timestamp']=1620297554
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=18']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=40
store['config']={'seed': 22, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4040708541870117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8182177543640137})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8356027603149414})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.934849739074707})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6696, 'crossentropy': 2.2352109375}
store['active_learning_steps'][0]['acquisition']={'indices': [7979, 28761, 34678, 10361, 49149, 28652, 12377, 5063, 46036, 28713, 55311, 27181, 47605, 59757, 47919, 1981, 32784, 5409, 11373, 13203], 'labels': [8, 9, 8, 9, 3, 4, 3, 9, 2, 9, 8, 2, 3, 2, 5, 3, 8, 8, 9, 0], 'scores': [1.269101321697235, 1.2596640586853027, 1.2362804412841797, 1.2229562997817993, 1.2196778059005737, 1.2196155786514282, 1.2094642519950867, 1.1986318230628967, 1.1940993666648865, 1.1922162175178528, 1.1900898814201355, 1.1869300603866577, 1.1770248413085938, 1.1763045191764832, 1.172423541545868, 1.1700567603111267, 1.168411135673523, 1.1674631237983704, 1.166950523853302, 1.166215717792511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.833040714263916})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4062302112579346})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.5424256324768066})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.871079921722412})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6734, 'crossentropy': 1.6156484375}
store['active_learning_steps'][1]['acquisition']={'indices': [47089, 34946, 21457, 37946, 45617, 14644, 13464, 53460, 28824, 36562, 21529, 34706, 47139, 49824, 36167, 43656, 44606, 53344, 17520, 48752], 'labels': [4, 8, 8, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 8, 2, 8, 0, 0, 2, 8], 'scores': [0.9179527759552002, 0.8976864814758301, 0.8795349597930908, 0.8734396696090698, 0.8717795610427856, 0.8679412603378296, 0.8672714233398438, 0.8661571741104126, 0.8630615472793579, 0.8537334203720093, 0.8520795702934265, 0.8517138361930847, 0.8504477739334106, 0.8487539887428284, 0.8475869297981262, 0.846899151802063, 0.8462258577346802, 0.8452587127685547, 0.842689573764801, 0.8411175608634949]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.523523211479187})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.173983097076416})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.155302047729492})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.268716335296631})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7067, 'crossentropy': 1.41664150390625}
store['active_learning_steps'][2]['acquisition']={'indices': [8886, 57236, 37552, 22743, 15116, 19586, 31962, 11202, 48548, 34332, 48341, 14795, 14866, 53316, 26838, 18402, 47689, 39266, 20039, 32070], 'labels': [2, 9, 5, 7, 5, 9, 3, 9, 9, 9, 7, 7, 7, 5, 7, 7, 3, 8, 7, 1], 'scores': [0.893663763999939, 0.8932803273200989, 0.8807137608528137, 0.8694643974304199, 0.8663135766983032, 0.8626700043678284, 0.8568771481513977, 0.8532224893569946, 0.8515819907188416, 0.8509469032287598, 0.8413336277008057, 0.8344030976295471, 0.8329991102218628, 0.8329524397850037, 0.8303741216659546, 0.8293044567108154, 0.8258773684501648, 0.8257557153701782, 0.8250980973243713, 0.8242008686065674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.5225441455841064})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.679991364479065})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.7903773784637451})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.0139834880828857})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7168, 'crossentropy': 1.34694111328125}
store['active_learning_steps'][3]['acquisition']={'indices': [42763, 12223, 28455, 22269, 8586, 12345, 30798, 59368, 4646, 36150, 5000, 59617, 22747, 53911, 40609, 13335, 29338, 11675, 10986, 55174], 'labels': [7, 2, 5, 2, 9, 3, 7, 5, 2, 7, 7, 7, 4, 7, 6, 0, 7, 0, 7, 7], 'scores': [0.8572567701339722, 0.8484698534011841, 0.809609591960907, 0.804316520690918, 0.7933056354522705, 0.792100191116333, 0.7909044623374939, 0.7862120866775513, 0.7829700708389282, 0.7824685573577881, 0.7784929275512695, 0.7726435661315918, 0.7714275121688843, 0.7712334990501404, 0.7701305150985718, 0.7700327634811401, 0.7692743539810181, 0.7653157711029053, 0.7638227343559265, 0.7632933855056763]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.196706771850586})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.418590784072876})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2318711280822754})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.3530807495117188})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7466, 'crossentropy': 1.0939046875}
store['active_learning_steps'][4]['acquisition']={'indices': [38529, 25187, 17301, 111, 38565, 51986, 3719, 11708, 49784, 49537, 58149, 1994, 25377, 26449, 25331, 33593, 12080, 4823, 3791, 47787], 'labels': [3, 3, 3, 3, 3, 2, 2, 3, 5, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 2], 'scores': [0.7589660882949829, 0.7572226524353027, 0.7497177720069885, 0.7380276322364807, 0.7367770671844482, 0.7361821532249451, 0.729536771774292, 0.7172567844390869, 0.7158340811729431, 0.7095761299133301, 0.7086341381072998, 0.7076756954193115, 0.7055070400238037, 0.7039092779159546, 0.7023534774780273, 0.6982030868530273, 0.694373369216919, 0.6927929520606995, 0.692783534526825, 0.6884428262710571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0838265419006348})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0285207033157349})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2329089641571045})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2894524335861206})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1548471450805664})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8252, 'crossentropy': 0.92170703125}
store['active_learning_steps'][5]['acquisition']={'indices': [12196, 134, 3070, 28371, 14125, 36744, 39487, 7984, 34520, 45446, 33150, 43711, 55591, 17958, 13030, 4784, 8892, 14113, 966, 46776], 'labels': [2, 1, 1, 3, 2, 1, 2, 4, 6, 7, 8, 3, 5, 9, 0, 7, 8, 2, 3, 8], 'scores': [1.09450101852417, 1.0274765491485596, 1.021962583065033, 1.0081672072410583, 0.9891154170036316, 0.9758530259132385, 0.954559862613678, 0.9482987523078918, 0.9447327852249146, 0.9372896552085876, 0.9315734505653381, 0.9286603927612305, 0.9285377264022827, 0.9231905937194824, 0.9189888834953308, 0.9160361289978027, 0.9153918623924255, 0.9153461456298828, 0.9121533036231995, 0.9115074276924133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.164332389831543})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1143290996551514})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.176164150238037})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1231929063796997})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2664344310760498})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8219, 'crossentropy': 0.9594498046875}
store['active_learning_steps'][6]['acquisition']={'indices': [30441, 8704, 16051, 12181, 29239, 11822, 21333, 1674, 59297, 9665, 30996, 3644, 45057, 20470, 57718, 57979, 4081, 20170, 38974, 19298], 'labels': [1, 1, 4, 5, 1, 7, 7, 9, 1, 7, 1, 1, 8, 3, 7, 1, 7, 9, 1, 6], 'scores': [0.8427770733833313, 0.8376331925392151, 0.8337637186050415, 0.8282845616340637, 0.8209323883056641, 0.8144873976707458, 0.813673198223114, 0.8133940100669861, 0.8123553395271301, 0.8112180233001709, 0.8111127018928528, 0.8102509379386902, 0.8099831938743591, 0.8089556694030762, 0.8088886141777039, 0.808771550655365, 0.8058841228485107, 0.8046225905418396, 0.8002024292945862, 0.7982808351516724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.077866792678833})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.842919111251831})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7725088596343994})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9030423760414124})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9014551043510437})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8996433019638062})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8868, 'crossentropy': 0.686804833984375}
store['active_learning_steps'][7]['acquisition']={'indices': [42121, 42237, 9370, 42317, 52169, 42703, 12985, 34829, 40599, 26733, 32724, 52959, 11581, 52686, 21023, 13253, 24632, 5013, 57345, 45410], 'labels': [5, 5, 4, 5, 2, 0, 2, 5, 5, 2, 5, 2, 2, 5, 2, 5, 2, 2, 5, 6], 'scores': [0.9398471117019653, 0.9229081869125366, 0.9212430715560913, 0.9159740209579468, 0.9060405492782593, 0.9060370922088623, 0.8982232809066772, 0.8967312574386597, 0.8940897583961487, 0.8925387263298035, 0.8817243576049805, 0.8809168338775635, 0.8794782757759094, 0.8738470077514648, 0.8733984231948853, 0.8690299987792969, 0.8635355830192566, 0.8623096346855164, 0.8609256148338318, 0.8608746528625488]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.038110613822937})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6814368367195129})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.693825900554657})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8209404945373535})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8099017143249512})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.631903271484375}
store['active_learning_steps'][8]['acquisition']={'indices': [17209, 34328, 35435, 55128, 22561, 58422, 43772, 17213, 6474, 41933, 17043, 5474, 49395, 54483, 13831, 17603, 27317, 5842, 46126, 32757], 'labels': [1, 8, 1, 8, 6, 9, 5, 1, 6, 5, 1, 8, 1, 5, 3, 0, 5, 1, 3, 5], 'scores': [0.8812257647514343, 0.8802874088287354, 0.8244343996047974, 0.8133034706115723, 0.8022958636283875, 0.793599545955658, 0.7851091027259827, 0.7787867188453674, 0.7759013175964355, 0.7750524282455444, 0.7711523771286011, 0.7710031270980835, 0.7691223621368408, 0.7661575675010681, 0.7651493549346924, 0.7601025700569153, 0.7592217922210693, 0.7585197687149048, 0.7582144737243652, 0.7562311291694641]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.044590711593628})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7126274108886719})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6743248105049133})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7196450233459473})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7737123966217041})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8225240707397461})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8983, 'crossentropy': 0.6283763671875}
store['active_learning_steps'][9]['acquisition']={'indices': [18240, 17494, 28512, 50320, 44466, 37574, 15948, 42948, 38698, 5684, 55491, 49616, 5679, 45602, 25422, 16488, 12305, 3615, 17079, 53872], 'labels': [3, 5, 5, 5, 4, 5, 2, 6, 5, 6, 8, 7, 3, 5, 6, 9, 9, 6, 6, 8], 'scores': [0.9413205981254578, 0.9286559820175171, 0.9283146262168884, 0.8777139782905579, 0.8733011484146118, 0.8687976598739624, 0.8669052720069885, 0.863442599773407, 0.8629616498947144, 0.8601825833320618, 0.8590572476387024, 0.8570771813392639, 0.8556264042854309, 0.8505182862281799, 0.8471506834030151, 0.8461398482322693, 0.844296932220459, 0.8423192501068115, 0.8412715792655945, 0.8408183455467224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1538869142532349})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7335313558578491})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6721481084823608})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6458466649055481})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6183261871337891})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7185764312744141})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7324521541595459})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7400330901145935})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.551640380859375}
store['active_learning_steps'][10]['acquisition']={'indices': [12748, 32323, 2423, 20037, 51415, 30884, 49487, 20989, 36884, 42161, 27281, 55001, 11625, 14650, 8443, 47925, 32309, 33505, 15723, 47680], 'labels': [0, 5, 3, 8, 0, 2, 8, 3, 2, 3, 0, 2, 8, 4, 2, 3, 8, 2, 8, 4], 'scores': [1.0652868151664734, 1.0197962522506714, 1.001990020275116, 1.0007537603378296, 0.992590069770813, 0.9901614785194397, 0.9897490739822388, 0.9844394326210022, 0.9811798930168152, 0.9748358726501465, 0.9720244109630585, 0.9690492749214172, 0.9616271257400513, 0.9594497084617615, 0.9591509699821472, 0.9585761427879333, 0.9572433233261108, 0.9572291374206543, 0.9506005644798279, 0.9503317475318909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.225705623626709})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6164904236793518})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5707646012306213})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5260264873504639})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5443907380104065})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5509108304977417})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5611395835876465})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.50162099609375}
store['active_learning_steps'][11]['acquisition']={'indices': [43745, 3810, 56457, 7160, 49460, 14558, 2064, 16117, 52582, 45764, 40589, 38882, 9180, 24006, 39899, 18324, 22083, 50898, 16953, 17777], 'labels': [8, 3, 3, 1, -1, 3, 7, 9, 2, 3, 2, 3, 3, 9, 2, 0, 2, 2, 9, 3], 'scores': [0.9567374587059021, 0.9407178163528442, 0.9406452775001526, 0.9151564240455627, 0.9075713157653809, 0.9071233868598938, 0.9055346548557281, 0.9018527269363403, 0.8977571129798889, 0.8974689841270447, 0.8911030292510986, 0.8906207084655762, 0.8880255222320557, 0.8828551173210144, 0.8772108554840088, 0.8744655847549438, 0.8722357153892517, 0.8674319386482239, 0.8670501708984375, 0.8653189539909363]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1302646398544312})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6754058003425598})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.530377984046936})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4877932071685791})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5090836882591248})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4806899130344391})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.527684211730957})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5297616720199585})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5098456144332886})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9334, 'crossentropy': 0.46182841796875}
store['active_learning_steps'][12]['acquisition']={'indices': [47626, 13942, 26358, 42415, 30692, 12650, 12663, 10070, 18501, 51863, 57728, 36126, 4036, 25873, 22272, 18487, 5163, 10044, 37450, 45065], 'labels': [-1, 4, 3, 7, 3, 5, 8, 9, 4, 9, 9, 5, -1, 8, 5, 4, 8, 6, 4, -1], 'scores': [1.0155878067016602, 0.9997405409812927, 0.9819235801696777, 0.9747381210327148, 0.9690908789634705, 0.9685927033424377, 0.9615952372550964, 0.9596483111381531, 0.9544105529785156, 0.9535844922065735, 0.9526390433311462, 0.9510287046432495, 0.950081467628479, 0.9487661123275757, 0.9468324184417725, 0.9382143616676331, 0.935772180557251, 0.9355298280715942, 0.9326006770133972, 0.9320673942565918]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.218418836593628})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6106531620025635})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5539455413818359})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5162115693092346})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49430131912231445})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5440714955329895})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.533383846282959})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5471364259719849})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.475155224609375}
store['active_learning_steps'][13]['acquisition']={'indices': [29899, 55244, 6418, 30357, 57242, 13428, 56249, 28745, 30585, 1075, 56030, 45924, 40654, 29335, 23958, 17121, 729, 32215, 26705, 49890], 'labels': [3, 7, 5, 7, 5, 9, -1, 7, -1, 7, 7, -1, 5, 8, -1, 8, -1, 7, 7, 5], 'scores': [0.988166332244873, 0.9369605779647827, 0.9250852465629578, 0.9138645529747009, 0.9136216044425964, 0.9114837050437927, 0.9094796776771545, 0.9084210395812988, 0.8989282846450806, 0.894210696220398, 0.8904013633728027, 0.8902139663696289, 0.8892537355422974, 0.8891208171844482, 0.885634183883667, 0.87921142578125, 0.8791868090629578, 0.8766684532165527, 0.8732925653457642, 0.8716613054275513]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.175650715827942})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6278259754180908})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.436548113822937})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4422622621059418})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40730607509613037})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40706515312194824})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39629608392715454})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44361698627471924})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4000183641910553})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4462311863899231})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.437060400390625}
store['active_learning_steps'][14]['acquisition']={'indices': [27335, 50736, 9774, 41540, 25462, 20869, 34847, 38389, 47674, 15432, 30451, 47626, 59747, 46132, 56066, 47387, 35694, 15779, 18193, 25218], 'labels': [4, -1, 7, 2, 6, 3, 0, 7, 4, 4, 8, -1, 5, 7, 7, 8, 9, 0, -1, 4], 'scores': [1.0460934042930603, 1.0249240398406982, 1.019167959690094, 1.0151728987693787, 1.0112619400024414, 0.986769437789917, 0.980378270149231, 0.9753825068473816, 0.9698784351348877, 0.9688832759857178, 0.9684505462646484, 0.967126190662384, 0.9610641598701477, 0.958243727684021, 0.9581206440925598, 0.9575135111808777, 0.9524700045585632, 0.9517834186553955, 0.9482153654098511, 0.9477030038833618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.078458309173584})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6656407117843628})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48695772886276245})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4033578038215637})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44267958402633667})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42277389764785767})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3883644640445709})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45097988843917847})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4230654835700989})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41747432947158813})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9535, 'crossentropy': 0.39799619140625}
store['active_learning_steps'][15]['acquisition']={'indices': [7851, 31308, 9552, 16572, 53054, 15913, 1568, 37962, 32880, 44661, 45048, 56662, 47626, 31474, 49660, 13998, 2148, 57311, 47383, 17358], 'labels': [8, 8, 0, 4, -1, 9, 4, 8, 0, 1, 4, 0, -1, 8, 8, 9, 6, 5, 6, 8], 'scores': [1.064054012298584, 1.044370412826538, 0.982586145401001, 0.9570386409759521, 0.9449844360351562, 0.9393710494041443, 0.936275839805603, 0.9344246983528137, 0.9124837517738342, 0.9122461080551147, 0.9110462963581085, 0.9070374369621277, 0.8972451090812683, 0.8959676623344421, 0.8927853107452393, 0.8875629901885986, 0.8857991695404053, 0.8838861584663391, 0.8833019137382507, 0.8823693990707397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9743170738220215})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5351409912109375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4438183307647705})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4097438454627991})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41482359170913696})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37736940383911133})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3338477611541748})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4206048250198364})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41741156578063965})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33703023195266724})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9535, 'crossentropy': 0.366087255859375}
store['active_learning_steps'][16]['acquisition']={'indices': [12577, 12687, 52889, 46832, 24533, 45944, 16756, 50917, 22531, 11482, 8765, 23890, 42020, 14152, 24469, 46938, 20641, 42838, 58980, 605], 'labels': [4, 4, -1, 7, 8, 9, 7, 4, 4, 8, 3, -1, 9, 7, 3, 7, 9, 9, 4, 4], 'scores': [1.0139628052711487, 1.0002897381782532, 0.9959079623222351, 0.9834380149841309, 0.9767829775810242, 0.9736207127571106, 0.9722412824630737, 0.9676054120063782, 0.9617753624916077, 0.95814049243927, 0.9580188393592834, 0.9502084255218506, 0.9408574104309082, 0.9394019246101379, 0.9338643550872803, 0.933062732219696, 0.9328904747962952, 0.9321494102478027, 0.9309772849082947, 0.9265092611312866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1959469318389893})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6682608127593994})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.47822996973991394})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40644270181655884})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.385237455368042})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39839550852775574})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4367067217826843})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40930095314979553})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9517, 'crossentropy': 0.3993991455078125}
store['active_learning_steps'][17]['acquisition']={'indices': [47626, 32776, 27358, 5443, 32668, 32573, 21601, 3367, 1352, 33812, 56006, 51266, 19025, 29672, 57507, 26822, 40398, 35246, 4153, 22193], 'labels': [-1, 4, 8, -1, 9, 8, 1, 0, 9, 6, 3, -1, 8, 9, 0, -1, -1, 8, 2, 5], 'scores': [1.0152925848960876, 0.9275984764099121, 0.9082635045051575, 0.9054532647132874, 0.8939173817634583, 0.88271164894104, 0.8787907361984253, 0.876926064491272, 0.8754847645759583, 0.8732767105102539, 0.8675981760025024, 0.8663452863693237, 0.8663244247436523, 0.8619109988212585, 0.8601804971694946, 0.8592348098754883, 0.8592342734336853, 0.8592072129249573, 0.8585945963859558, 0.8552524447441101]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.2556278705596924})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6206470727920532})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48647916316986084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.34006252884864807})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36193543672561646})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3548627495765686})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3021823763847351})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.38118046522140503})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32368481159210205})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3345806896686554})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.32213349609375}
store['active_learning_steps'][18]['acquisition']={'indices': [7259, 41802, 4741, 48360, 17478, 24462, 19590, 5600, 36363, 47926, 17855, 57742, 34828, 44286, 24522, 41108, 5790, 49915, 42438, 51266], 'labels': [2, 2, 6, 3, 4, 2, 5, 6, 6, 8, 6, 6, -1, 8, 6, 0, 2, 6, 9, -1], 'scores': [0.9586630463600159, 0.952568531036377, 0.9489284157752991, 0.9332418441772461, 0.9265022277832031, 0.9143778085708618, 0.9128785133361816, 0.8989499807357788, 0.8963737487792969, 0.8934775590896606, 0.8928024768829346, 0.8898033499717712, 0.8773353695869446, 0.8770327568054199, 0.8695128560066223, 0.8693536520004272, 0.865428626537323, 0.8628101944923401, 0.8621740341186523, 0.8586594462394714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1569950580596924})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5587115287780762})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42067089676856995})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3408687114715576})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3294697403907776})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3232741951942444})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33886903524398804})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3537461757659912})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3482205271720886})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.318426611328125}
store['active_learning_steps'][19]['acquisition']={'indices': [52690, 19089, 13388, 47626, 1573, 53844, 50946, 36078, 21382, 13969, 3798, 46368, 54892, 34771, 35710, 53990, 8762, 58560, 59286, 44378], 'labels': [3, 5, 3, -1, 2, 5, 3, 3, 2, 3, 7, 8, 3, 0, 1, -1, 3, 0, 8, 7], 'scores': [0.9675176739692688, 0.9209402799606323, 0.9125082492828369, 0.8942298889160156, 0.879302978515625, 0.8758643865585327, 0.8758211731910706, 0.8686190247535706, 0.8679401278495789, 0.8636053204536438, 0.8446645736694336, 0.8445287346839905, 0.8433442711830139, 0.8429337739944458, 0.8419287204742432, 0.8384928703308105, 0.8358825445175171, 0.835202693939209, 0.8341269493103027, 0.8335663080215454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1938893795013428})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6309380531311035})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.4632209539413452})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4428367614746094})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33410996198654175})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3694741129875183})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.322451114654541})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37134140729904175})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33755064010620117})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3035372495651245})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3506850004196167})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.39233219623565674})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.34533700346946716})
store['active_learning_steps'][20]['training']['best_epoch']=10
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.3308970703125}
store['active_learning_steps'][20]['acquisition']={'indices': [5891, 37469, 20110, 14619, 37048, 31345, 14655, 35269, 54814, 38932, 20967, 52899, 48102, 23967, 24031, 635, 20820, 5265, 1812, 6011], 'labels': [4, 2, 4, 3, 9, 3, 3, -1, 4, 5, 2, 7, 7, -1, 6, 5, 9, 4, 4, -1], 'scores': [1.0031837224960327, 0.9761571884155273, 0.9709506630897522, 0.9657410383224487, 0.9552834033966064, 0.9537659883499146, 0.9486976265907288, 0.9413108825683594, 0.93972247838974, 0.9349479079246521, 0.9280086755752563, 0.9243555068969727, 0.9220818281173706, 0.9147303104400635, 0.9143498539924622, 0.914268434047699, 0.9108357429504395, 0.9107910990715027, 0.9059351086616516, 0.9043917655944824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.164910912513733})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6263295412063599})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4733648896217346})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40435218811035156})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37162214517593384})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35839611291885376})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3521157503128052})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3147236704826355})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3466190993785858})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4008059501647949})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3751791715621948})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3387001953125}
store['active_learning_steps'][21]['acquisition']={'indices': [14896, 19546, 46021, 52889, 52294, 7949, 24740, 43897, 4822, 15771, 40066, 4663, 42557, 20635, 45666, 14894, 32016, 52851, 1600, 29379], 'labels': [8, 9, 9, -1, 0, -1, 8, 1, 4, 5, 4, 9, 9, 5, 1, 5, 9, 2, 0, 9], 'scores': [0.9531121253967285, 0.900871217250824, 0.8967890739440918, 0.8966134190559387, 0.8889252543449402, 0.8877737522125244, 0.8814812302589417, 0.8793001770973206, 0.8776108622550964, 0.8772223591804504, 0.8713736534118652, 0.8694541454315186, 0.8691534399986267, 0.8677091598510742, 0.8655219078063965, 0.8647868633270264, 0.8628237843513489, 0.8620674014091492, 0.8576219081878662, 0.8479906320571899]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1008225679397583})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6424652934074402})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4513920545578003})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35329246520996094})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3987368643283844})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3357747197151184})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3671550750732422})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33058303594589233})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3060253858566284})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.32644128799438477})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3498454689979553})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33954137563705444})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.3042145263671875}
store['active_learning_steps'][22]['acquisition']={'indices': [11616, 788, 52086, 4379, 8883, 30900, 31252, 52800, 53990, 27716, 13021, 11271, 19868, 10744, 21134, 5851, 41464, 5536, 340, 34314], 'labels': [7, 9, 5, -1, 2, 5, 5, 9, -1, 7, 5, -1, 5, 7, 4, 7, 8, 8, 7, 7], 'scores': [1.0015618801116943, 0.9776296615600586, 0.9647036194801331, 0.9615073204040527, 0.928717851638794, 0.9283304214477539, 0.9220162034034729, 0.9177029728889465, 0.9155910611152649, 0.9116522073745728, 0.9107441306114197, 0.9098270535469055, 0.9068200886249542, 0.904260516166687, 0.9034497737884521, 0.9020082354545593, 0.9017031192779541, 0.8952533602714539, 0.8951464295387268, 0.8894228935241699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.253636360168457})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6579505205154419})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4727609157562256})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4028153419494629})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3793798089027405})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33268922567367554})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37087470293045044})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3924524188041687})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36030113697052})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.322400732421875}
store['active_learning_steps'][23]['acquisition']={'indices': [45972, 48378, 41283, 57956, 29132, 12808, 52889, 47036, 16731, 10982, 58734, 49002, 52834, 56612, 44969, 5052, 39778, 343, 1512, 2381], 'labels': [2, 2, 3, 2, 8, 2, -1, 2, -1, 1, 8, 1, 2, 2, 3, 0, 8, -1, 0, 7], 'scores': [0.8669534921646118, 0.8404163718223572, 0.8371820449829102, 0.8298763036727905, 0.8232059478759766, 0.8152469396591187, 0.8138386011123657, 0.8127439022064209, 0.7972084879875183, 0.7967070937156677, 0.7958633303642273, 0.7953677177429199, 0.7919327020645142, 0.7900099158287048, 0.7871848344802856, 0.7870479822158813, 0.7864924073219299, 0.7834305167198181, 0.7828789949417114, 0.7820066809654236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2072019577026367})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.708419680595398})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4662590026855469})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40256983041763306})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38597169518470764})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34389528632164})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3046935796737671})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3144243657588959})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3194733262062073})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33007103204727173})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.3079250732421875}
