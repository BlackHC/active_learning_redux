store = {}
store['timestamp']=1620297322
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=17']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=17
store['worker_id']=17
store['num_workers']=40
store['config']={'seed': 21, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.227459192276001})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.048830509185791})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.0878915786743164})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1286063194274902})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6614, 'crossentropy': 2.06256171875}
store['active_learning_steps'][0]['acquisition']={'indices': [19042, 22845, 35340, 18042, 15798, 56664, 22662, 56857, 5017, 22169], 'labels': [9, 5, 2, 0, 0, 2, 7, 0, 9, 2], 'scores': [1.0960093140602112, 1.0853149890899658, 1.0704963207244873, 1.0695761442184448, 1.067238688468933, 1.0634950995445251, 1.0608455538749695, 1.057886779308319, 1.0578468441963196, 1.0571466088294983]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.0033974647521973})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2657270431518555})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.600841999053955})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.356484889984131})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6889, 'crossentropy': 1.853625390625}
store['active_learning_steps'][1]['acquisition']={'indices': [6894, 12947, 20037, 36766, 25521, 25039, 12663, 20170, 34524, 16010], 'labels': [3, 0, 8, 6, 5, 0, 8, 9, 8, 5], 'scores': [1.1319937705993652, 1.1220412254333496, 1.115335464477539, 1.1141372919082642, 1.1048961877822876, 1.1036657094955444, 1.0979199409484863, 1.0976477265357971, 1.0943167805671692, 1.0891084671020508]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8814293146133423})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9329051971435547})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.1822633743286133})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2966060638427734})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6398, 'crossentropy': 1.87296015625}
store['active_learning_steps'][2]['acquisition']={'indices': [56891, 24391, 9588, 38298, 32355, 6348, 52771, 46447, 27181, 25387], 'labels': [8, 4, 7, 5, 8, 2, 3, 2, 2, 8], 'scores': [0.9417006969451904, 0.9393123388290405, 0.9354254007339478, 0.9261183142662048, 0.922507643699646, 0.9220558404922485, 0.9216352701187134, 0.9168280363082886, 0.9133739471435547, 0.9110745191574097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.819809913635254})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.4147019386291504})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.513874053955078})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.7116572856903076})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6907, 'crossentropy': 1.69041484375}
store['active_learning_steps'][3]['acquisition']={'indices': [3370, 43904, 32976, 37751, 30350, 17945, 42671, 25315, 15551, 46580], 'labels': [4, 4, 4, 6, 6, 2, 2, 5, 4, 6], 'scores': [0.9032331705093384, 0.899039089679718, 0.8904167413711548, 0.8799302577972412, 0.8783004283905029, 0.8737921714782715, 0.8725678324699402, 0.8716766834259033, 0.8702259063720703, 0.8555712103843689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.397017240524292})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.590104341506958})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.592408299446106})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.773336410522461})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7631, 'crossentropy': 1.2597078125}
store['active_learning_steps'][4]['acquisition']={'indices': [21315, 53976, 14705, 34429, 24486, 14729, 54994, 36562, 12716, 56362], 'labels': [8, 9, 0, 4, 6, 0, 6, 0, 0, 0], 'scores': [0.8653321266174316, 0.8347463011741638, 0.8323147296905518, 0.8018690347671509, 0.7992636561393738, 0.7987320423126221, 0.790614128112793, 0.7836804389953613, 0.7803176045417786, 0.7798174023628235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.2869913578033447})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.6109135150909424})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8136980533599854})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.7520182132720947})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7595, 'crossentropy': 1.22415419921875}
store['active_learning_steps'][5]['acquisition']={'indices': [19869, 27420, 42639, 43818, 19823, 934, 19942, 826, 40437, 31844], 'labels': [7, 3, 7, 2, 7, 7, 5, 9, 8, 7], 'scores': [0.8265856504440308, 0.8178562521934509, 0.8030846118927002, 0.8002181649208069, 0.7990264296531677, 0.7928242683410645, 0.7911502122879028, 0.7906655073165894, 0.7818311452865601, 0.7800309658050537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0403846502304077})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2367310523986816})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1292470693588257})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2190937995910645})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8049, 'crossentropy': 0.92901123046875}
store['active_learning_steps'][6]['acquisition']={'indices': [8958, 46832, 111, 49824, 36744, 14065, 4665, 28371, 23112, 14689], 'labels': [3, 7, 3, 8, 1, 3, 5, 3, 8, 5], 'scores': [0.7835726737976074, 0.7471041679382324, 0.7470057010650635, 0.7417906522750854, 0.7373232841491699, 0.7257325649261475, 0.7124841213226318, 0.7091842889785767, 0.7067523002624512, 0.7026541233062744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9627443552017212})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9604213833808899})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1219029426574707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1863501071929932})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.224177360534668})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8449, 'crossentropy': 0.86065322265625}
store['active_learning_steps'][7]['acquisition']={'indices': [24479, 31335, 11983, 47021, 37596, 34877, 13827, 10871, 32319, 57311], 'labels': [8, 5, 5, 5, 7, 5, 3, 5, 3, 5], 'scores': [0.93010413646698, 0.9190936088562012, 0.9098740816116333, 0.9070292711257935, 0.9011178016662598, 0.8908756971359253, 0.8907617330551147, 0.8892499208450317, 0.8889435529708862, 0.8885300159454346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0318800210952759})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0439101457595825})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0500233173370361})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0866994857788086})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8028, 'crossentropy': 0.9699923828125}
store['active_learning_steps'][8]['acquisition']={'indices': [52169, 38275, 3765, 12305, 49525, 53131, 42199, 46329, 49545, 11257], 'labels': [2, 2, 2, 9, 8, 8, 3, 3, 8, 2], 'scores': [0.7255573272705078, 0.7079998254776001, 0.6983966827392578, 0.6916136741638184, 0.688386082649231, 0.6854053735733032, 0.6843429803848267, 0.6833287477493286, 0.6832213401794434, 0.678907036781311]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0104402303695679})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8732084035873413})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9970454573631287})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.075803518295288})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2540407180786133})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8568, 'crossentropy': 0.766867529296875}
store['active_learning_steps'][9]['acquisition']={'indices': [28373, 58537, 25844, 27139, 3352, 13074, 35232, 11572, 21058, 40030], 'labels': [4, 5, 4, 5, 4, 0, 8, 5, 5, 4], 'scores': [0.9230767488479614, 0.8714611530303955, 0.8491571545600891, 0.8419970273971558, 0.836585283279419, 0.8288332223892212, 0.8251756429672241, 0.816865861415863, 0.8155236840248108, 0.8147295117378235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.06535804271698})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9291239976882935})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1381876468658447})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1185214519500732})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1444816589355469})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8413, 'crossentropy': 0.829822265625}
store['active_learning_steps'][10]['acquisition']={'indices': [41999, 43525, 49537, 44948, 49199, 37048, 52358, 8680, 31090, 51464], 'labels': [0, 8, 2, 9, 0, 9, 2, 8, 4, 0], 'scores': [0.9390305280685425, 0.9025328159332275, 0.8938838243484497, 0.8780056834220886, 0.8774093389511108, 0.8725273013114929, 0.862692654132843, 0.8559511303901672, 0.8548251986503601, 0.8501045107841492]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9727609753608704})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8370566964149475})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8529377579689026})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9670474529266357})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9208438992500305})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8473, 'crossentropy': 0.75113505859375}
store['active_learning_steps'][11]['acquisition']={'indices': [6174, 21355, 59370, 14841, 55612, 14428, 42828, 18720, 9555, 21023], 'labels': [9, 0, 7, 7, 9, 5, 7, 7, 9, 2], 'scores': [0.8533849716186523, 0.8483995199203491, 0.8470907211303711, 0.8428749442100525, 0.8285056352615356, 0.8280515670776367, 0.8120787739753723, 0.8094775676727295, 0.800841748714447, 0.7891110181808472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9545866250991821})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8014093637466431})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8000068664550781})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9319815635681152})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8877670764923096})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0083531141281128})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.7153365234375}
store['active_learning_steps'][12]['acquisition']={'indices': [35401, 56379, 5013, 3273, 7033, 59289, 49915, 19896, 17756, 1812], 'labels': [3, 4, 2, 8, 7, 1, 6, 6, 8, 4], 'scores': [0.9982461333274841, 0.905590295791626, 0.9053734540939331, 0.9032385945320129, 0.9025270342826843, 0.8902899622917175, 0.8871120810508728, 0.8782826662063599, 0.8766591548919678, 0.8760511875152588]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9566419124603271})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7274810671806335})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8017805218696594})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7555305361747742})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7615790367126465})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8749, 'crossentropy': 0.70603310546875}
store['active_learning_steps'][13]['acquisition']={'indices': [51764, 37574, 49616, 1127, 2000, 59468, 21270, 12066, 42428, 38760], 'labels': [5, 5, 7, 7, 5, 7, 4, 8, 5, 9], 'scores': [0.8673673868179321, 0.8649994730949402, 0.8100566267967224, 0.8049741983413696, 0.802200198173523, 0.7990032434463501, 0.7901782989501953, 0.7831602096557617, 0.7737289667129517, 0.7727447748184204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.955980122089386})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6418853998184204})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6318447589874268})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6552925109863281})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6390169858932495})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6798447370529175})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.89, 'crossentropy': 0.6198611328125}
store['active_learning_steps'][14]['acquisition']={'indices': [11600, 25986, 16627, 23020, 36515, 44172, 45800, 43176, 46368, 34520], 'labels': [2, 8, 2, 2, 3, 8, 9, 2, 8, 6], 'scores': [0.9681163430213928, 0.9407028555870056, 0.9298666715621948, 0.9242165088653564, 0.9041258096694946, 0.9019224643707275, 0.88901287317276, 0.8886876702308655, 0.8875977993011475, 0.8865832686424255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.1629488468170166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7288975715637207})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.725937008857727})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7542890906333923})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8325295448303223})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.769071102142334})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8844, 'crossentropy': 0.706380078125}
store['active_learning_steps'][15]['acquisition']={'indices': [2381, 37465, 42263, 51986, 14972, 19111, 21335, 32880, 56190, 40593], 'labels': [7, 5, 4, 2, 4, 4, 7, 0, 4, 4], 'scores': [0.9619258046150208, 0.8987323641777039, 0.8986766934394836, 0.8914638757705688, 0.8825294375419617, 0.8749585151672363, 0.8631634712219238, 0.8600447773933411, 0.8591974973678589, 0.8572564721107483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.0826654434204102})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6288982629776001})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6862536668777466})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5802013278007507})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7385380268096924})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7842864990234375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.813213586807251})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9069, 'crossentropy': 0.59137705078125}
store['active_learning_steps'][16]['acquisition']={'indices': [46126, 15848, 39526, 20322, 47260, 43043, 52106, 9778, 14765, 1239], 'labels': [3, 3, 5, 1, 6, 3, 5, 3, 3, 8], 'scores': [1.05394446849823, 0.9270641207695007, 0.9133898615837097, 0.9020327925682068, 0.8936059474945068, 0.8923373222351074, 0.8923080563545227, 0.8888826966285706, 0.8840887546539307, 0.8829396963119507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0180001258850098})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7985165119171143})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6616120934486389})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7077983617782593})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6870702505111694})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8836944699287415})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8896, 'crossentropy': 0.630491552734375}
store['active_learning_steps'][17]['acquisition']={'indices': [39480, 50930, 17539, 42746, 3691, 42703, 12089, 19960, 57659, 17941], 'labels': [9, 0, 0, 2, 0, 0, 3, 6, 0, 0], 'scores': [0.8584791421890259, 0.8485327363014221, 0.8313660621643066, 0.8209100365638733, 0.8103821873664856, 0.8102357387542725, 0.8073098659515381, 0.8011639714241028, 0.8007290959358215, 0.7896916270256042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0837644338607788})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7305036783218384})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6921066045761108})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6907133460044861})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7758158445358276})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7760173082351685})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8381035923957825})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8983, 'crossentropy': 0.671759521484375}
store['active_learning_steps'][18]['acquisition']={'indices': [52889, 18150, 22561, 47626, 34828, 33594, 50736, 48397, 36417, 14385], 'labels': [-1, 8, 6, -1, -1, 3, -1, 5, 6, 8], 'scores': [0.9807167053222656, 0.9603635668754578, 0.9542285203933716, 0.9493210315704346, 0.9466037154197693, 0.9375920295715332, 0.9230939149856567, 0.8928269147872925, 0.885699450969696, 0.8836634755134583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.1375927925109863})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6817007064819336})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6446071863174438})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6559631824493408})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6452348232269287})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7272775173187256})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.6330013671875}
store['active_learning_steps'][19]['acquisition']={'indices': [59297, 49202, 195, 56041, 1674, 16628, 42311, 11406, 50461, 32712], 'labels': [1, 5, 9, 9, 9, 9, 9, 8, 7, 8], 'scores': [0.9134531021118164, 0.8997410535812378, 0.8797860741615295, 0.8786368370056152, 0.8629603385925293, 0.8575770854949951, 0.847748339176178, 0.8473166227340698, 0.8459525108337402, 0.8340966701507568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2052922248840332})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6776741743087769})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5968092679977417})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6169475317001343})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5834217071533203})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7553091049194336})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6214852333068848})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6411672830581665})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.572180712890625}
store['active_learning_steps'][20]['acquisition']={'indices': [26444, 12514, 59726, 52889, 30884, 9340, 39561, 39668, 49539, 29376], 'labels': [1, 2, 5, -1, 2, 5, 2, 8, 6, -1], 'scores': [0.9952121376991272, 0.943568229675293, 0.9400701522827148, 0.9332766532897949, 0.9331120848655701, 0.9318382740020752, 0.9245030879974365, 0.9171072244644165, 0.916873574256897, 0.9168211817741394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0316040515899658})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6830431222915649})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5753836631774902})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5102559328079224})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5384204387664795})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6050735116004944})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5996026396751404})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9307, 'crossentropy': 0.477140771484375}
store['active_learning_steps'][21]['acquisition']={'indices': [47626, 45917, 26358, 4379, 35269, 42632, 53979, 51759, 47741, 8932], 'labels': [-1, 9, 3, -1, -1, 0, 8, 3, 5, 0], 'scores': [0.9567514061927795, 0.9048864841461182, 0.8930614590644836, 0.8818508386611938, 0.8722472786903381, 0.8674609661102295, 0.8571856021881104, 0.856249988079071, 0.8510497808456421, 0.8501310348510742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2242006063461304})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6817995309829712})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5375806093215942})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5055347084999084})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5042232275009155})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.513756275177002})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44694507122039795})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4792342782020569})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5376249551773071})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5247998237609863})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9395, 'crossentropy': 0.443891357421875}
store['active_learning_steps'][22]['acquisition']={'indices': [4822, 4185, 47626, 18398, 52889, 22866, 22139, 7984, 57387, 22742], 'labels': [4, 2, -1, 4, -1, 5, 2, 4, 2, 2], 'scores': [1.092622995376587, 1.0695261359214783, 1.0582577586174011, 1.0260530710220337, 1.0101497173309326, 1.0028477311134338, 0.9986997246742249, 0.992773175239563, 0.9695735573768616, 0.9659395813941956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.201648235321045})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5810714960098267})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6902720928192139})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5734138488769531})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5586363673210144})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5645518898963928})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5604070425033569})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6020482778549194})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.52813642578125}
store['active_learning_steps'][23]['acquisition']={'indices': [56196, 37129, 40378, 10884, 40466, 17382, 5163, 36990, 20526, 23890], 'labels': [-1, 8, -1, 5, 8, 6, 8, -1, -1, -1], 'scores': [0.9701648950576782, 0.9458460807800293, 0.9452223777770996, 0.9377719759941101, 0.9348779320716858, 0.8925929665565491, 0.8852752447128296, 0.8789173364639282, 0.8771554231643677, 0.8755633234977722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.1910340785980225})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7110318541526794})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5293388366699219})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49275609850883484})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5597759485244751})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.442740797996521})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5907340049743652})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5882622003555298})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6350288987159729})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9334, 'crossentropy': 0.459743212890625}
store['active_learning_steps'][24]['acquisition']={'indices': [36818, 31345, 5443, 47626, 9390, 44736, 29899, 52889, 20641, 48260], 'labels': [7, 3, -1, -1, -1, 5, 3, -1, 9, 5], 'scores': [1.1479264497756958, 1.0586749911308289, 1.0360696911811829, 1.0253150463104248, 1.0249003171920776, 1.0228880047798157, 1.017819881439209, 1.0160857439041138, 1.013436734676361, 1.0129731595516205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1387214660644531})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6032954454421997})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.47527116537094116})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.521602988243103})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5115360617637634})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5211907029151917})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.479758154296875}
store['active_learning_steps'][25]['acquisition']={'indices': [15942, 29938, 43588, 18003, 13259, 4955, 19188, 14305, 32668, 37120], 'labels': [4, 9, 8, 2, 1, 2, 1, 8, 9, 2], 'scores': [0.828596830368042, 0.8084665536880493, 0.8048521280288696, 0.8002838492393494, 0.795478105545044, 0.792730987071991, 0.7912893891334534, 0.7909461855888367, 0.78825843334198, 0.7814614772796631]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.276412844657898})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6445357799530029})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49790215492248535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4353088140487671})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4508664608001709})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46404117345809937})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4426528811454773})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9418, 'crossentropy': 0.436290673828125}
store['active_learning_steps'][26]['acquisition']={'indices': [20172, 29303, 29286, 51903, 28859, 49890, 5821, 4646, 6291, 3146], 'labels': [4, 8, 9, 3, 2, 5, 7, 2, 3, 9], 'scores': [0.9133394956588745, 0.8887317180633545, 0.877730131149292, 0.8759422302246094, 0.8707952499389648, 0.8644651174545288, 0.8623509407043457, 0.8604170680046082, 0.8602244853973389, 0.8570467829704285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.113590121269226})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5518826246261597})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5064696669578552})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45229828357696533})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4573204219341278})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38260263204574585})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4790576994419098})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49465590715408325})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4952351152896881})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.380904833984375}
store['active_learning_steps'][27]['acquisition']={'indices': [31738, 5175, 2803, 5293, 29294, 34946, 50317, 6347, 42337, 42317], 'labels': [8, 4, 3, 4, 3, 8, 3, 3, 5, 5], 'scores': [0.9979224801063538, 0.9870486259460449, 0.9701683521270752, 0.9640435576438904, 0.9508504867553711, 0.9492543935775757, 0.9490830898284912, 0.9313937425613403, 0.9273001551628113, 0.924801766872406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.242174744606018})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.63446044921875})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4967588186264038})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4660857319831848})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4979650378227234})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.42061594128608704})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4662019908428192})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4878004491329193})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.49565204977989197})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9561, 'crossentropy': 0.4218466796875}
store['active_learning_steps'][28]['acquisition']={'indices': [47036, 3730, 58660, 59314, 25332, 36363, 49499, 58832, 41426, 55906], 'labels': [2, 8, 3, 9, 2, 6, 1, 3, 4, 2], 'scores': [1.0060734152793884, 0.9974137544631958, 0.9939414858818054, 0.969904363155365, 0.9680271744728088, 0.9535273909568787, 0.9476541876792908, 0.943044900894165, 0.9419060349464417, 0.9406524896621704]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2969940900802612})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6293161511421204})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4825805425643921})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.45666569471359253})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4183630347251892})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45377838611602783})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4305369257926941})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40669137239456177})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39478370547294617})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4169636368751526})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4635728597640991})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4780194163322449})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9564, 'crossentropy': 0.375272314453125}
store['active_learning_steps'][29]['acquisition']={'indices': [57972, 42503, 26568, 7949, 20110, 32445, 57718, 32776, 3367, 53054], 'labels': [4, 2, -1, -1, 4, 5, 7, 4, 0, -1], 'scores': [1.0549490451812744, 0.9928804337978363, 0.9898675680160522, 0.9868883490562439, 0.9780935645103455, 0.965774416923523, 0.9593170881271362, 0.9576653838157654, 0.9504761695861816, 0.9478723406791687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4087960720062256})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6354576349258423})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5465943813323975})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5300110578536987})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.434892475605011})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41040778160095215})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4539918899536133})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43647122383117676})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42867469787597656})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.402988134765625}
store['active_learning_steps'][30]['acquisition']={'indices': [15832, 52889, 39488, 23550, 317, 52550, 37122, 45189, 19663, 360], 'labels': [9, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [1.0700969099998474, 1.0556479096412659, 0.993262767791748, 0.9925751686096191, 0.9788312911987305, 0.9723427295684814, 0.9690827131271362, 0.9657444357872009, 0.9651303291320801, 0.9632297158241272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4322388172149658})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7430484294891357})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5707007050514221})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5100614428520203})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4380302429199219})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4272763431072235})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4284822940826416})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4010790288448334})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.47041964530944824})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4653272032737732})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4033932089805603})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9578, 'crossentropy': 0.392159619140625}
store['active_learning_steps'][31]['acquisition']={'indices': [36704, 50736, 47626, 14210, 7949, 57211, 55131, 9776, 37441, 6818], 'labels': [2, -1, -1, -1, -1, 5, -1, -1, 1, -1], 'scores': [1.0382319688796997, 1.0078261494636536, 1.0004656314849854, 0.9961560964584351, 0.9867875576019287, 0.9839061498641968, 0.9757540822029114, 0.9744102358818054, 0.9734326601028442, 0.9733747839927673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3139625787734985})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6767497658729553})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44916826486587524})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4208519458770752})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4293164312839508})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38687664270401})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4110124111175537})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38469719886779785})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3808850646018982})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3869767189025879})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4020434617996216})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3423137962818146})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3650599420070648})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4315931797027588})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4381687045097351})
store['active_learning_steps'][32]['training']['best_epoch']=12
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.3358409912109375}
store['active_learning_steps'][32]['acquisition']={'indices': [53872, 8447, 54433, 59747, 55739, 24894, 37583, 9458, 14843, 55339], 'labels': [8, 3, -1, 5, 5, -1, -1, -1, 9, -1], 'scores': [1.1287760734558105, 1.0672548413276672, 1.0653660297393799, 1.060713291168213, 1.0426781177520752, 1.0266976356506348, 1.026402473449707, 1.0144412517547607, 1.0064338445663452, 1.0012702941894531]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3796968460083008})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.617619514465332})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4454658627510071})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45362764596939087})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4641505479812622})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4008921682834625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.384086549282074})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4037800133228302})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41361910104751587})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38411232829093933})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.360618115234375}
store['active_learning_steps'][33]['acquisition']={'indices': [47626, 41933, 1642, 35269, 13376, 14894, 38698, 8505, 27358, 602], 'labels': [-1, 5, 6, -1, 3, 5, 5, -1, 8, 8], 'scores': [1.0639486908912659, 1.0201875567436218, 0.9801276326179504, 0.9760663509368896, 0.971902072429657, 0.9689550399780273, 0.9683272242546082, 0.963276207447052, 0.9593788385391235, 0.9577930569648743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.3339039087295532})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7286579608917236})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5437099933624268})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4676505923271179})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4371705651283264})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3646607995033264})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41805821657180786})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40965861082077026})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41329628229141235})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.3300147705078125}
store['active_learning_steps'][34]['acquisition']={'indices': [23140, 13942, 22497, 28368, 53054, 57195, 5303, 30851, 34078, 46995], 'labels': [7, 4, 7, 9, -1, 3, -1, -1, 2, -1], 'scores': [0.9666774868965149, 0.9375267028808594, 0.9110815525054932, 0.8792708516120911, 0.8540080189704895, 0.8396280407905579, 0.8378493785858154, 0.8374950289726257, 0.8357101678848267, 0.8343026041984558]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3424487113952637})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.718379020690918})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.584484338760376})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46117156744003296})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40407174825668335})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43193089962005615})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38806435465812683})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41049832105636597})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43705782294273376})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4837057888507843})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.958, 'crossentropy': 0.38651943359375}
store['active_learning_steps'][35]['acquisition']={'indices': [21601, 52294, 28392, 13149, 32335, 51266, 17518, 28302, 58560, 34328], 'labels': [1, 0, 3, 7, 1, -1, 0, -1, 0, 8], 'scores': [0.9860115051269531, 0.9818054437637329, 0.9451689720153809, 0.9379433393478394, 0.9317352771759033, 0.9314905405044556, 0.9314321875572205, 0.9258105754852295, 0.9257209897041321, 0.9255986213684082]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.324953556060791})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5715371370315552})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4813166856765747})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4723094403743744})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4078422784805298})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3890657126903534})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3588121831417084})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40672796964645386})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3676246404647827})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3437904119491577})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4181573987007141})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33287692070007324})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36285072565078735})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4418022632598877})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37477803230285645})
store['active_learning_steps'][36]['training']['best_epoch']=12
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.310583056640625}
store['active_learning_steps'][36]['acquisition']={'indices': [5247, 13156, 37469, 39429, 35326, 7949, 54378, 48540, 27429, 27791], 'labels': [2, 2, 2, 2, 5, -1, 7, 8, 0, -1], 'scores': [1.003146767616272, 0.9976486563682556, 0.9954056143760681, 0.9947986602783203, 0.9918605089187622, 0.9821261167526245, 0.9734092950820923, 0.9726501107215881, 0.956145167350769, 0.950142502784729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.242836833000183})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6235687732696533})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46065032482147217})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45732468366622925})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38505423069000244})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3733633756637573})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3507283926010132})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4020616114139557})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3966110348701477})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3502262830734253})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4172600507736206})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3873211741447449})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35473987460136414})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9605, 'crossentropy': 0.374272314453125}
store['active_learning_steps'][37]['acquisition']={'indices': [47626, 32747, 42415, 21896, 14210, 8704, 9407, 56249, 20703, 18501], 'labels': [-1, 8, 7, 8, -1, 1, -1, -1, -1, 4], 'scores': [1.040463387966156, 1.0354096293449402, 1.0348816514015198, 1.0238775610923767, 1.0185347199440002, 1.0111476182937622, 1.0055676698684692, 1.0021291375160217, 1.0000932812690735, 0.9991129040718079]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.149041771888733})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6268819570541382})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41541555523872375})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.361514151096344})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37551775574684143})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3784078359603882})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41006195545196533})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.3592418701171875}
store['active_learning_steps'][38]['acquisition']={'indices': [47626, 2782, 45171, 46186, 46995, 4153, 31014, 56196, 42673, 4564], 'labels': [-1, -1, -1, -1, -1, 2, -1, -1, -1, -1], 'scores': [1.0003927946090698, 0.9684587717056274, 0.9463107585906982, 0.9372144341468811, 0.9327880144119263, 0.92957603931427, 0.8991838693618774, 0.8967903256416321, 0.896092414855957, 0.88944411277771]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2957544326782227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6530133485794067})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46344006061553955})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4555988311767578})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4045959711074829})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3926430940628052})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.368871808052063})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43036043643951416})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3870173394680023})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3682129383087158})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.49037909507751465})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.39772289991378784})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39069023728370667})
store['active_learning_steps'][39]['training']['best_epoch']=10
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.3183644287109375}
store['active_learning_steps'][39]['acquisition']={'indices': [7949, 11482, 47626, 45666, 52889, 50736, 42472, 48975, 13995, 49828], 'labels': [-1, 8, -1, 1, -1, -1, 2, 2, -1, -1], 'scores': [1.0942201018333435, 1.0686911344528198, 0.9994325637817383, 0.9892327189445496, 0.9858476519584656, 0.9754470586776733, 0.9734936952590942, 0.9691401720046997, 0.9685047268867493, 0.9668678641319275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3831872940063477})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7257956862449646})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4535384178161621})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43301844596862793})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41375303268432617})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4352772831916809})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39574629068374634})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3959669768810272})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40049776434898376})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3594602346420288})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3919064402580261})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4221540093421936})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.44725218415260315})
store['active_learning_steps'][40]['training']['best_epoch']=10
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.3488720703125}
store['active_learning_steps'][40]['acquisition']={'indices': [29180, 57882, 42673, 9384, 47626, 29357, 16446, 29161, 53693, 17079], 'labels': [9, 0, -1, 5, -1, -1, 5, -1, 4, 6], 'scores': [1.05711829662323, 1.0255433320999146, 1.0200153589248657, 1.0187996923923492, 1.0131884217262268, 1.0082462430000305, 0.991115152835846, 0.990607500076294, 0.9873434901237488, 0.9868251085281372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3669743537902832})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7111037969589233})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.556419849395752})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3930312991142273})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36667388677597046})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3685733675956726})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3621302843093872})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.371111661195755})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39148658514022827})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.373060941696167})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.3589134521484375}
store['active_learning_steps'][41]['acquisition']={'indices': [49501, 7949, 360, 51744, 33812, 5679, 50231, 49573, 37122, 43745], 'labels': [4, -1, -1, -1, 6, 3, 8, 2, -1, 8], 'scores': [1.021448016166687, 0.9610945582389832, 0.960708737373352, 0.9543153047561646, 0.9494563341140747, 0.9493194222450256, 0.9428890347480774, 0.9396290183067322, 0.9360510110855103, 0.9311060905456543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4102091789245605})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7052411437034607})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5626099109649658})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5024690628051758})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45885324478149414})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3597428798675537})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41096770763397217})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45537495613098145})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38432908058166504})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.347446142578125}
store['active_learning_steps'][42]['acquisition']={'indices': [9180, 35128, 45602, 7949, 16731, 7829, 43034, 26635, 27540, 4379], 'labels': [3, 2, 5, -1, -1, -1, 9, 2, -1, -1], 'scores': [0.9459962248802185, 0.8886404633522034, 0.885579526424408, 0.8749369382858276, 0.868261992931366, 0.8644817471504211, 0.8551604747772217, 0.8501758575439453, 0.8493787050247192, 0.8475829362869263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4437929391860962})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7945308685302734})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5564017295837402})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4396688938140869})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4026781916618347})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4413667321205139})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3857576847076416})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4110783338546753})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4317600727081299})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40312719345092773})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.342856005859375}
store['active_learning_steps'][43]['acquisition']={'indices': [45749, 52889, 36939, 53357, 50459, 45469, 1598, 19537, 6011, 55618], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, -1, -1], 'scores': [1.030846655368805, 0.9878842830657959, 0.9698745608329773, 0.9634668827056885, 0.9557236433029175, 0.9470987319946289, 0.945894181728363, 0.9415918588638306, 0.9329969882965088, 0.9316680431365967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4521148204803467})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6829864978790283})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49526795744895935})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.392702579498291})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3930121958255768})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3770756125450134})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35530775785446167})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33171766996383667})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3802027702331543})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3650858998298645})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3966093957424164})
store['active_learning_steps'][44]['training']['best_epoch']=8
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.292067333984375}
store['active_learning_steps'][44]['acquisition']={'indices': [44873, 38990, 3136, 326, 12184, 43059, 40732, 7886, 11074, 52223], 'labels': [-1, 3, 6, -1, 0, 0, 0, 9, 9, -1], 'scores': [0.9715164303779602, 0.9690939784049988, 0.9569550156593323, 0.9460197687149048, 0.9379010796546936, 0.9312324523925781, 0.9298965334892273, 0.9267960786819458, 0.9183001518249512, 0.9148041009902954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4645640850067139})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.7509415149688721})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4529467225074768})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42776986956596375})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34377244114875793})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3579830527305603})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3440687656402588})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36912453174591064})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.3264896484375}
store['active_learning_steps'][45]['acquisition']={'indices': [7438, 48096, 8214, 45446, 4784, 40654, 29320, 46088, 23678, 42113], 'labels': [7, 7, 7, 7, 7, 5, 1, 6, 7, -1], 'scores': [0.8868389129638672, 0.8518937826156616, 0.8487029671669006, 0.8439452052116394, 0.8062054514884949, 0.8047986030578613, 0.801266074180603, 0.8005279302597046, 0.7990903258323669, 0.7857462167739868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.3999372720718384})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.713971734046936})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.540905237197876})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39614343643188477})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3669072389602661})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3610960841178894})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3762897849082947})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36906635761260986})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3474792242050171})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.402361124753952})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.39720356464385986})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.40040162205696106})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.3459036865234375}
store['active_learning_steps'][46]['acquisition']={'indices': [54628, 52306, 13878, 27024, 51600, 9390, 40022, 36822, 32419, 28930], 'labels': [4, 8, 4, 8, 4, 9, 8, 1, 4, 7], 'scores': [1.0623891353607178, 0.9529263377189636, 0.9491583108901978, 0.9473538994789124, 0.9147052764892578, 0.9120376110076904, 0.9096208810806274, 0.906644880771637, 0.8984054327011108, 0.8979529738426208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.303220510482788})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6497334837913513})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.45071130990982056})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3962962031364441})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34239813685417175})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3585047721862793})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32519495487213135})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32872986793518066})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33423513174057007})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3004578948020935})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32876041531562805})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3304055333137512})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2952234745025635})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30694738030433655})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3146662712097168})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30940961837768555})
store['active_learning_steps'][47]['training']['best_epoch']=13
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.2684403076171875}
store['active_learning_steps'][47]['acquisition']={'indices': [15779, 45749, 32583, 4564, 46133, 22098, 22607, 46021, 40398, 56196], 'labels': [0, -1, -1, -1, -1, -1, 4, 9, -1, -1], 'scores': [1.0253716707229614, 1.016552448272705, 1.0117348432540894, 1.0082812309265137, 0.9996042251586914, 0.9934423565864563, 0.9916957020759583, 0.9882932305335999, 0.9867515563964844, 0.9829424023628235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.455796480178833})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7701389789581299})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5058982968330383})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.41315144300460815})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38569390773773193})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38165825605392456})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3670442998409271})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35685765743255615})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32551002502441406})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3516885042190552})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3361477851867676})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3568660616874695})
store['active_learning_steps'][48]['training']['best_epoch']=9
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.3009859130859375}
store['active_learning_steps'][48]['acquisition']={'indices': [5974, 49518, 48160, 57221, 52800, 31184, 59378, 54652, 45502, 5440], 'labels': [-1, -1, -1, -1, 9, 9, -1, -1, 1, -1], 'scores': [0.9256709218025208, 0.8999639749526978, 0.8937554359436035, 0.8926045298576355, 0.8782094717025757, 0.8755632042884827, 0.8721133470535278, 0.8682283759117126, 0.8672516345977783, 0.8622105121612549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.3519693613052368})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6760871410369873})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4832903742790222})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40596866607666016})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38991400599479675})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3589048385620117})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37432268261909485})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39348095655441284})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3818720877170563})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9642, 'crossentropy': 0.321519970703125}
store['active_learning_steps'][49]['acquisition']={'indices': [47626, 53357, 59081, 28216, 52686, 20903, 15771, 28512, 49002, 1872], 'labels': [-1, -1, -1, -1, 5, 3, 5, 5, 1, 3], 'scores': [0.837100625038147, 0.8230915069580078, 0.8211293816566467, 0.8199785947799683, 0.8084222674369812, 0.8072940111160278, 0.8025869131088257, 0.7879704833030701, 0.7810760736465454, 0.7806989550590515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3816685676574707})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7361750602722168})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.5749706029891968})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41890615224838257})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3666394352912903})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34480321407318115})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3466326594352722})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.37074097990989685})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3786903917789459})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.3180082275390625}
store['active_learning_steps'][50]['acquisition']={'indices': [11292, 5315, 55244, 41789, 13995, 44753, 34406, 6574, 13969, 41713], 'labels': [1, 3, 7, 0, -1, 5, 4, -1, 3, 0], 'scores': [0.8711175322532654, 0.8340392112731934, 0.8226661086082458, 0.8199551105499268, 0.8150103092193604, 0.8122143745422363, 0.8098477721214294, 0.80937659740448, 0.8089166283607483, 0.8074426651000977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.3996613025665283})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.7651547789573669})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.45503532886505127})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4205096364021301})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3499550223350525})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34120890498161316})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3323562741279602})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31218141317367554})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34325724840164185})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3072384297847748})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3520856499671936})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3765573799610138})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3446331322193146})
store['active_learning_steps'][51]['training']['best_epoch']=10
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.268534765625}
store['active_learning_steps'][51]['acquisition']={'indices': [59081, 14210, 45409, 1598, 4123, 54885, 14266, 53990, 15754, 5974], 'labels': [-1, -1, -1, -1, -1, 6, 3, -1, -1, -1], 'scores': [1.0640810132026672, 1.0049748420715332, 0.9890204071998596, 0.988772988319397, 0.9856778383255005, 0.9841275215148926, 0.9805548191070557, 0.9719418287277222, 0.971847414970398, 0.9661086201667786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.3801839351654053})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.7143282890319824})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5150445103645325})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42756348848342896})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3588342070579529})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3631581664085388})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33399856090545654})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31588876247406006})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34406134486198425})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.33069267868995667})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3296045660972595})
store['active_learning_steps'][52]['training']['best_epoch']=8
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2844894287109375}
store['active_learning_steps'][52]['acquisition']={'indices': [5298, 26376, 48404, 8228, 45409, 20169, 7949, 635, 22824, 22098], 'labels': [0, 1, -1, 3, -1, 4, -1, 5, 9, -1], 'scores': [0.9191247224807739, 0.9079775214195251, 0.8796615600585938, 0.8753944039344788, 0.8658676147460938, 0.8612217307090759, 0.8596054911613464, 0.8587090969085693, 0.8530982136726379, 0.8500432968139648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.3572918176651})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6467205882072449})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4692727327346802})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38958168029785156})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3063620924949646})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.289884477853775})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32897821068763733})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33195143938064575})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3310627341270447})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.27820966796875}
store['active_learning_steps'][53]['acquisition']={'indices': [36268, 19244, 56643, 13318, 32047, 18487, 29376, 27898, 14152, 15386], 'labels': [5, 9, 2, 6, 9, 4, -1, 2, 7, 6], 'scores': [0.8534694314002991, 0.8477365970611572, 0.823652982711792, 0.8217571377754211, 0.8063806295394897, 0.7836349606513977, 0.7812291979789734, 0.7775828838348389, 0.77126145362854, 0.7699563503265381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3598899841308594})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6225370168685913})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.45701295137405396})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3968481421470642})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3591616153717041})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31583738327026367})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3215876817703247})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30160242319107056})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31030774116516113})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29971441626548767})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2846413552761078})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31801682710647583})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2856513559818268})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33573970198631287})
store['active_learning_steps'][54]['training']['best_epoch']=11
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.280302197265625}
store['active_learning_steps'][54]['acquisition']={'indices': [7949, 6846, 29672, 4741, 33780, 51863, 32918, 35654, 31591, 828], 'labels': [-1, 2, 9, 6, 8, 9, 2, 1, 8, 4], 'scores': [0.9862241148948669, 0.9763891398906708, 0.9584048986434937, 0.9579349756240845, 0.9366275072097778, 0.9240593910217285, 0.911794126033783, 0.9106439352035522, 0.906897783279419, 0.9037219285964966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3858921527862549})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7252087593078613})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.500680685043335})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42968568205833435})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3835199475288391})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4124496579170227})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.343583345413208})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3762284517288208})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33952516317367554})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3293273150920868})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.33806827664375305})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32843321561813354})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3122522830963135})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.33170920610427856})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3613388240337372})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.373401403427124})
store['active_learning_steps'][55]['training']['best_epoch']=13
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.3033715576171875}
store['active_learning_steps'][55]['acquisition']={'indices': [52228, 29903, 17779, 12198, 19789, 27576, 59701, 53993, 340, 56480], 'labels': [0, 0, 0, -1, -1, 5, 5, 6, 7, 9], 'scores': [1.1006819009780884, 1.0127767324447632, 1.0120666027069092, 1.0005029439926147, 0.9838718771934509, 0.983001708984375, 0.9820482134819031, 0.9792717099189758, 0.9777673482894897, 0.9613845646381378]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4186832904815674})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6951064467430115})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5020554065704346})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.4304928779602051})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33820512890815735})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31035566329956055})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3160056471824646})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3253079652786255})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3164031207561493})
store['active_learning_steps'][56]['training']['best_epoch']=6
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.3103067626953125}
store['active_learning_steps'][56]['acquisition']={'indices': [588, 29352, 46274, 24462, 12302, 17712, 15781, 8606, 41295, 4638], 'labels': [2, 3, 7, 2, 2, 3, 5, 3, 9, 3], 'scores': [0.8821475505828857, 0.8322433233261108, 0.8132941126823425, 0.8111388087272644, 0.800056517124176, 0.7880894541740417, 0.774931788444519, 0.7748945355415344, 0.774637758731842, 0.7743546366691589]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.441338062286377})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.7429719567298889})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.5255733132362366})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.40135008096694946})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3597666025161743})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3275125324726105})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2829332947731018})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2549763321876526})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2597576975822449})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26919040083885193})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.270363450050354})
store['active_learning_steps'][57]['training']['best_epoch']=8
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.275700732421875}
